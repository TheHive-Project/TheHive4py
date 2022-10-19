from typing import Optional

from requests import Response


class TheHiveError(Exception):
    """Base error class for TheHive API."""

    def __init__(
        self, message: str, response: Optional[Response] = None, *args, **kwargs
    ):
        super().__init__(message, *args, **kwargs)
        self.message = message
        self.response = response
