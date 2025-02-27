"""Sync client for TheHive API."""

from typing import Optional

from thehive4py.base.client_base import TheHiveApiBase
from thehive4py.session import TheHiveSession, RetryValue, VerifyValue


class TheHiveApi(TheHiveApiBase):
    def _get_session(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify: VerifyValue = True,
        max_retries: RetryValue = 5,
        timeout: int = 30,
    ) -> TheHiveSession:
        """Create and return a sync session."""
        return TheHiveSession(
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            verify=verify,
            max_retries=max_retries,
        )
