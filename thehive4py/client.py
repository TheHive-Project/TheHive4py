from typing import Optional

from thehive4py.endpoints import (
    AlertEndpoint,
    CaseEndpoint,
    CaseTemplateEndpoint,
    CommentEndpoint,
    ObservableEndpoint,
    OrganisationEndpoint,
    ProcedureEndpoint,
    ProfileEndpoint,
    TaskEndpoint,
    TaskLogEndpoint,
    TimelineEndpoint,
    UserEndpoint,
)
from thehive4py.endpoints.cortex import CortexEndpoint
from thehive4py.endpoints.custom_field import CustomFieldEndpoint
from thehive4py.endpoints.misp import MISPEndpoint
from thehive4py.endpoints.observable_type import ObservableTypeEndpoint
from thehive4py.endpoints.page_template import PageTemplateEndpoint
from thehive4py.endpoints.query import QueryEndpoint
from thehive4py.session import DEFAULT_RETRY, RetryValue, TheHiveSession, VerifyValue


class TheHiveApi:
    def __init__(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        organisation: Optional[str] = None,
        verify: VerifyValue = True,
        max_retries: RetryValue = DEFAULT_RETRY,
    ):
        """Create a client of TheHive API.

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
            max_retries: Either `None`, in which case we do not retry failed requests,
                or a `Retry` object.

        """
        self.session = TheHiveSession(
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            verify=verify,
            max_retries=max_retries,
        )
        self.session_organisation = organisation

        # case management endpoints
        self.alert = AlertEndpoint(self.session)
        self.case = CaseEndpoint(self.session)
        self.case_template = CaseTemplateEndpoint(self.session)
        self.comment = CommentEndpoint(self.session)
        self.observable = ObservableEndpoint(self.session)
        self.page_template = PageTemplateEndpoint(self.session)
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
        self.misp = MISPEndpoint(self.session)

        # standard endpoints
        self.query = QueryEndpoint(self.session)

    @property
    def session_organisation(self) -> Optional[str]:
        return self.session.headers.get("X-Organisation")  # type:ignore

    @session_organisation.setter
    def session_organisation(self, organisation: Optional[str] = None):
        if organisation:
            self.session.headers["X-Organisation"] = organisation
        else:
            self.session.headers.pop("X-Organisation", None)
