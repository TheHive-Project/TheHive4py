"""Async session implementation for TheHive API."""

import ssl
from contextlib import asynccontextmanager
from os import PathLike
from typing import Any, Optional, Union

import aiohttp
from aiohttp.client import ClientTimeout

from thehive4py.errors import TheHiveError
from thehive4py.base.session_base import TheHiveSessionBase, RetryValue, VerifyValue


class TheHiveAsyncSession(TheHiveSessionBase):
    """Async session implementation using aiohttp."""

    def __init__(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify: VerifyValue = True,
        max_retries: RetryValue = 5,
        timeout: int = 30,
    ):
        super().__init__(
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            verify=verify,
            max_retries=max_retries,
        )
        self.timeout = ClientTimeout(total=timeout)

        # Set up SSL context
        if isinstance(verify, bool):
            self.ssl_context = None if verify else ssl.create_default_context()
            if not verify and self.ssl_context:
                self.ssl_context.check_hostname = False
                self.ssl_context.verify_mode = ssl.CERT_NONE
        elif isinstance(verify, str):
            self.ssl_context = ssl.create_default_context(cafile=verify)
        else:
            raise ValueError(
                "verify must be either a boolean or a string path to a CA bundle"
            )

    def _set_basic_auth(self, username: str, password: str) -> None:
        """Set basic auth header for aiohttp."""
        import base64

        auth = base64.b64encode(f"{username}:{password}".encode()).decode()
        self.headers["Authorization"] = f"Basic {auth}"

    async def make_request(
        self,
        method: str,
        path: str,
        params=None,
        data=None,
        json=None,
        files=None,
        download_path: Union[str, PathLike, None] = None,
    ) -> Any:
        """Make an async HTTP request."""
        endpoint_url = f"{self.hive_url}{path}"
        headers = {**self.headers}

        if json:
            data = self._encode_json(json)
            headers["Content-Type"] = "application/json"

        # Prepare form data if files are present
        form = None
        if files:
            form = aiohttp.FormData()
            if isinstance(files, dict):
                for key, file_tuple in files.items():
                    filename, filestream, content_type = file_tuple
                    form.add_field(
                        key, filestream, filename=filename, content_type=content_type
                    )
            elif isinstance(files, list):
                for field_name, file_tuple in files:
                    filename, filestream, content_type = file_tuple
                    form.add_field(
                        field_name,
                        filestream,
                        filename=filename,
                        content_type=content_type,
                    )

        for _ in range(self.max_retries + 1):
            try:
                async with aiohttp.ClientSession(
                    headers=headers, timeout=self.timeout
                ) as session:
                    async with session.request(
                        method,
                        endpoint_url,
                        params=params,
                        data=form if form else data,
                        ssl=self.ssl_context,
                    ) as response:
                        if download_path:
                            return await self._process_stream_response(
                                response, download_path
                            )
                        return await self._process_response(response)

            except aiohttp.ClientError as e:
                if _ == self.max_retries:
                    raise TheHiveError(
                        f"Request failed after {self.max_retries} retries: {str(e)}"
                    )
                continue

    async def _process_response(self, response: aiohttp.ClientResponse) -> Any:
        """Process the async response."""
        if response.ok:
            try:
                return await response.json()
            except aiohttp.ContentTypeError:
                return await response.text()

        try:
            error_json = await response.json()
            if isinstance(error_json, dict) and all(
                key in error_json for key in ["type", "message"]
            ):
                error_text = f"{error_json['type']} - {error_json['message']}"
            else:
                error_text = await response.text()
        except aiohttp.ContentTypeError:
            error_text = await response.text()

        raise TheHiveError(message=error_text, response=response)

    async def _process_stream_response(
        self, response: aiohttp.ClientResponse, download_path: Union[str, PathLike]
    ) -> None:
        """Process an async streaming response."""
        if not response.ok:
            await self._process_response(response)

        with open(download_path, "wb") as download_fp:
            async for chunk in response.content.iter_chunked(8192):
                download_fp.write(chunk)

    @asynccontextmanager
    async def session_context(self):
        """Create a shared session context for multiple requests."""
        async with aiohttp.ClientSession(
            headers=self.headers, timeout=self.timeout
        ) as session:
            yield session
