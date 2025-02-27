"""Async client for TheHive API."""

from typing import Optional

import certifi

from thehive4py.async_api.session import TheHiveAsyncSession
from thehive4py.base.client_base import TheHiveApiBase
from thehive4py.session import RetryValue, VerifyValue


class TheHiveAsyncApi(TheHiveApiBase):
    """Async client implementation that uses TheHiveAsyncSession."""

    def __init__(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        organisation: Optional[str] = None,
        verify: VerifyValue = certifi.where(),  # Set default to CA bundle
        max_retries: RetryValue = 5,
        timeout: int = 30,
    ):
        super().__init__(
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            organisation=organisation,
            verify=verify,  # Pass the CA bundle path to base class
            max_retries=max_retries,
            timeout=timeout,
        )

    def _get_session(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify: VerifyValue = certifi.where(),
        max_retries: RetryValue = 5,
        timeout: int = 30,
    ) -> TheHiveAsyncSession:
        return TheHiveAsyncSession(
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            verify=verify,
            max_retries=max_retries,
            timeout=timeout,
        )
