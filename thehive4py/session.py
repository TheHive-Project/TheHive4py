import json as jsonlib
from collections import UserDict
from json.decoder import JSONDecodeError

import requests
import requests.auth

from thehive4py.errors import TheHiveError


class SessionJSONEncoder(jsonlib.JSONEncoder):
    """Custom JSON encoder class for TheHive session."""

    def default(self, o):
        if isinstance(o, UserDict):
            return o.data
        return super().default(o)


class TheHiveSession(requests.Session):
    def __init__(
        self,
        url: str,
        apikey: str = None,
        username: str = None,
        password: str = None,
        organisation: str = None,
        verify=None,
    ):
        super().__init__()
        self.url = self._sanitize_url(url)
        self.verify = verify
        self.headers["User-Agent"] = f"thehive4py/{__version__}"

        if organisation:
            self.headers["X-Organisation"] = organisation
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

    def _sanitize_url(self, url: str) -> str:
        """Sanitize the base url for the client."""
        if url.endswith("/"):
            return url[:-1]
        return url

    def make_request(
        self,
        method: str,
        path: str,
        params=None,
        data=None,
        json=None,
    ):
        if path.startswith("/"):
            url = f"{self.url}{path}"
        else:
            url = f"{self.url}/api/v1/{path}"

        if json:
            data = jsonlib.dumps(json, cls=SessionJSONEncoder)
            self.headers["Content-Type"] = "application/json"

        response = self.request(
            method,
            url=url,
            params=params,
            data=data,
            headers=self.headers,
            verify=self.verify,
        )

        return self._process_response(response)

    def _process_response(self, response: requests.Response):
        try:
            json_data = response.json()
        except JSONDecodeError:
            json_data = None

        if response.status_code == 207:
            error_text = (
                f"{json_data['failure'][0]['type']} "
                f"- {json_data['failure'][0]['message']}"
            )
            raise TheHiveError(error_text)
        elif not response.ok:
            if json_data is None:
                error_text = response.text
            else:
                error_text = f"{json_data['type']} - {json_data['message']}"

            raise TheHiveError(error_text)
        else:
            if json_data is None:
                return response.text
            return json_data
