"""Base session class for TheHive API."""

import json as jsonlib

from abc import ABC, abstractmethod
from collections import UserDict
from os import PathLike
from typing import Any, Dict, Optional, Union

from thehive4py.__version__ import __version__
from thehive4py.errors import TheHiveError


RetryValue = Union[int, None]
VerifyValue = Union[bool, str]


class _SessionJSONEncoder(jsonlib.JSONEncoder):
    """Custom JSON encoder class for TheHive session."""

    def default(self, o: Any):
        if isinstance(o, UserDict):
            return o.data
        return super().default(o)


class TheHiveSessionBase(ABC):
    """Base session implementation shared by sync and async sessions."""

    def __init__(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify: VerifyValue = True,
        max_retries: RetryValue = 5,
    ):
        """Initialize base session.

        Parameters:
            url: TheHive's url.
            apikey: TheHive's apikey. Required if username/password not provided.
            username: TheHive's username. Required with password if apikey not provided.
            password: TheHive's password. Required with username if apikey not provided.
            verify: Either a boolean to control SSL verification, or path to CA bundle.
            max_retries: Maximum number of retries for failed requests.
        """
        self.hive_url = self._sanitize_hive_url(url)
        self.verify = verify
        self.max_retries = max_retries
        self.headers: Dict[str, str] = {"User-Agent": f"thehive4py/{__version__}"}

        if username and password:
            # For basic auth we'll let implementations handle it since
            # the auth header format might differ between sync/async
            self._set_basic_auth(username, password)
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

    def _encode_json(self, data: Any) -> str:
        """Encode data as JSON string using custom encoder."""
        return jsonlib.dumps(data, cls=_SessionJSONEncoder)

    @abstractmethod
    def _set_basic_auth(self, username: str, password: str) -> None:
        """Set basic auth header. Must be implemented by subclasses."""
        raise NotImplementedError

    @abstractmethod
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
        """Make a request. Must be implemented by subclasses."""
        raise NotImplementedError
