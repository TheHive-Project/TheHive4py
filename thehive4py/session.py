"""Sync session implementation for TheHive API."""

import requests
import requests.adapters
import requests.auth
from os import PathLike
from typing import Any, Optional, Union
from urllib3 import Retry

from thehive4py.errors import TheHiveError
from thehive4py.base.session_base import TheHiveSessionBase, RetryValue, VerifyValue


DEFAULT_RETRY = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
    raise_on_status=False,
)


class TheHiveSession(TheHiveSessionBase, requests.Session):
    """Sync session implementation using requests."""

    def __init__(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify: VerifyValue = True,
        max_retries: RetryValue = DEFAULT_RETRY,
    ):
        requests.Session.__init__(self)
        TheHiveSessionBase.__init__(
            self,
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            verify=verify,
            max_retries=max_retries,
        )
        self._set_retries(max_retries)

    def _set_basic_auth(self, username: str, password: str) -> None:
        """Set basic auth header using requests auth."""
        self.headers["Authorization"] = requests.auth._basic_auth_str(
            username, password
        )

    def _set_retries(self, max_retries: RetryValue):
        """Configure the session to retry."""
        retry_adapter = requests.adapters.HTTPAdapter(max_retries=max_retries)
        self.mount("http://", retry_adapter)
        self.mount("https://", retry_adapter)

    def make_request(
        self,
        method: str,
        path: str,
        params=None,
        data=None,
        json=None,
        files=None,
        download_path: Union[str, PathLike, None] = None,
    ) -> Any:
        """Make a sync HTTP request."""
        endpoint_url = f"{self.hive_url}{path}"
        headers = {**self.headers}

        if json:
            data = self._encode_json(json)
            headers["Content-Type"] = "application/json"

        response = self.request(
            method,
            url=endpoint_url,
            params=params,
            data=data,
            files=files,
            headers=headers,
            verify=self.verify,
            stream=bool(download_path),
        )

        return self._process_response(response, download_path=download_path)

    def _process_response(
        self,
        response: requests.Response,
        download_path: Union[str, PathLike, None] = None,
    ):
        """Process the sync response."""
        if response.ok:
            if download_path is None:
                return self._process_text_response(response)
            else:
                self._process_stream_response(
                    response=response, download_path=download_path
                )

        if not response.ok:
            self._process_error_response(response=response)

    def _process_text_response(self, response: requests.Response):
        """Process a text/json response."""
        try:
            json_data = response.json()
        except requests.exceptions.JSONDecodeError:
            json_data = None

        if json_data is None:
            return response.text
        return json_data

    def _process_stream_response(
        self, response: requests.Response, download_path: Union[str, PathLike]
    ):
        """Process a streaming response."""
        with open(download_path, "wb") as download_fp:
            for chunk in response.iter_content(chunk_size=4096):
                download_fp.write(chunk)

    def _process_error_response(self, response: requests.Response):
        """Process an error response."""
        try:
            json_data = response.json()
        except requests.exceptions.JSONDecodeError:
            json_data = None

        if isinstance(json_data, dict) and all(
            key in json_data for key in ["type", "message"]
        ):
            error_text = f"{json_data['type']} - {json_data['message']}"
        else:
            error_text = response.text
        raise TheHiveError(message=error_text, response=response)
