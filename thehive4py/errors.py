from typing import Optional

from requests import Response


class TheHiveError(Exception):
    def __init__(
        self, message: str, response: Optional[Response] = None, *args, **kwargs
    ):
        """Base error class of thehive4py.

        Args:
            message: The exception message.
            response: Either `None`, or a `Response` object of a failed request.
        """
        super().__init__(message, *args, **kwargs)
        self.message = message
        self.response = response
