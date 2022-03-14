import json as jsonlib
from collections import UserDict
from json.decoder import JSONDecodeError
from os import PathLike
from typing import Any, Optional, Union

import requests
import requests.auth

from thehive4py import __version__
from thehive4py.errors import TheHiveError


class SessionJSONEncoder(jsonlib.JSONEncoder):
    """Custom JSON encoder class for TheHive session."""

    def default(self, o: Any):
        if isinstance(o, UserDict):
            return o.data
        return super().default(o)


class TheHiveSession(requests.Session):
    def __init__(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify=None,
    ):
        super().__init__()
        self.hive_url = self._sanitize_hive_url(url)
        self.verify = verify
        self.headers["User-Agent"] = f"thehive4py/{__version__}"

        if username and password:
            self.headers["Authorization"] = requests.auth._basic_auth_str(
                username, password
            )
        elif apikey:
            self.headers["Authorization"] = f"Bearer {apikey}"
        else:
            raise TheHiveError(
                "Either apikey or the username/password combination must be provided!"
            )

    def _sanitize_hive_url(self, hive_url: str) -> str:
        """Sanitize the base url for the client."""
        if hive_url.endswith("/"):
            return hive_url[:-1]
        return hive_url

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

        endpoint_url = f"{self.hive_url}{path}"

        headers = {**self.headers}
        if json:
            data = jsonlib.dumps(json, cls=SessionJSONEncoder)
            headers = {**headers, "Content-Type": "application/json"}

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
        try:
            json_data = response.json()
        except JSONDecodeError:
            json_data = None

        if json_data is None:
            return response.text
        return json_data

    def _process_stream_response(
        self, response: requests.Response, download_path: Union[str, PathLike]
    ):
        with open(download_path, "wb") as download_fp:
            for chunk in response.iter_content(chunk_size=4096):
                download_fp.write(chunk)

    def _process_error_response(self, response: requests.Response):
        try:
            json_data = response.json()
        except JSONDecodeError:
            json_data = None

        if json_data is None:
            error_text = response.text
        else:
            error_text = f"{json_data['type']} - {json_data['message']}"
        raise TheHiveError(error_text)
