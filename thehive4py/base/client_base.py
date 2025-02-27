"""Base class for TheHive API clients."""

from abc import ABC, abstractmethod
from typing import Optional

from thehive4py.base.session_base import TheHiveSessionBase, VerifyValue, RetryValue
from thehive4py.endpoints.alert import AlertEndpoint
from thehive4py.endpoints.case import CaseEndpoint
from thehive4py.endpoints.case_template import CaseTemplateEndpoint
from thehive4py.endpoints.comment import CommentEndpoint
from thehive4py.endpoints.cortex import CortexEndpoint
from thehive4py.endpoints.custom_field import CustomFieldEndpoint
from thehive4py.endpoints.observable import ObservableEndpoint
from thehive4py.endpoints.observable_type import ObservableTypeEndpoint
from thehive4py.endpoints.organisation import OrganisationEndpoint
from thehive4py.endpoints.procedure import ProcedureEndpoint
from thehive4py.endpoints.profile import ProfileEndpoint
from thehive4py.endpoints.query import QueryEndpoint
from thehive4py.endpoints.task import TaskEndpoint
from thehive4py.endpoints.task_log import TaskLogEndpoint
from thehive4py.endpoints.timeline import TimelineEndpoint
from thehive4py.endpoints.user import UserEndpoint


class TheHiveApiBase(ABC):
    def __init__(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        organisation: Optional[str] = None,
        verify: VerifyValue = True,
        max_retries: RetryValue = 5,
        timeout: int = 30,
    ):
        """Initialize base TheHive API client.

        Parameters:
            url: TheHive's url.
            apikey: TheHive's apikey. It's required if `username` and `password`
                is not provided.
            username: TheHive's username. It's required if `apikey` is not provided.
                Must be specified together with `password`.
            password: TheHive's password. It's required if `apikey` is not provided.
                Must be specified together with `username`.
            organisation: TheHive organisation to use in the session.
            verify: Either a boolean, in which case it controls whether we verify
                the server's TLS certificate, or a string, in which case it must be a
                path to a CA bundle to use.
            max_retries: Maximum number of retries for failed requests.
            timeout: Request timeout in seconds.
        """
        self.session = self._get_session(
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            verify=verify,
            max_retries=max_retries,
            timeout=timeout,
        )
        self.session_organisation = organisation

        # case management endpoints
        self.alert = AlertEndpoint(self.session)
        self.case = CaseEndpoint(self.session)
        self.case_template = CaseTemplateEndpoint(self.session)
        self.comment = CommentEndpoint(self.session)
        self.observable = ObservableEndpoint(self.session)
        self.procedure = ProcedureEndpoint(self.session)
        self.task = TaskEndpoint(self.session)
        self.task_log = TaskLogEndpoint(self.session)
        self.timeline = TimelineEndpoint(self.session)

        # user management endpoints
        self.user = UserEndpoint(self.session)
        self.organisation = OrganisationEndpoint(self.session)
        self.profile = ProfileEndpoint(self.session)

        # entity endpoints
        self.custom_field = CustomFieldEndpoint(self.session)
        self.observable_type = ObservableTypeEndpoint(self.session)

        # connector endpoints
        self.cortex = CortexEndpoint(self.session)

        # standard endpoints
        self.query = QueryEndpoint(self.session)

    @abstractmethod
    def _get_session(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        verify: VerifyValue = True,
        max_retries: RetryValue = 5,
        timeout: int = 30,
    ) -> TheHiveSessionBase:  # type: ignore
        """Create and return a session object. Must be implemented by subclasses."""
        raise NotImplementedError

    @property
    def session_organisation(self) -> Optional[str]:
        return self.session.headers.get("X-Organisation")  # type:ignore

    @session_organisation.setter
    def session_organisation(self, organisation: Optional[str] = None):
        if organisation:
            self.session.headers["X-Organisation"] = organisation
        else:
            self.session.headers.pop("X-Organisation", None)
