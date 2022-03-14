from typing import Optional

from thehive4py.endpoints import (
    AlertEndpoint,
    CaseEndpoint,
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
from thehive4py.session import TheHiveSession


class TheHiveApi:
    def __init__(
        self,
        url: str,
        apikey: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        organisation: Optional[str] = None,
        verify=None,
    ):
        self.session = TheHiveSession(
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            verify=verify,
        )
        self.session_organisation = organisation

        # case management endpoints
        self.alert = AlertEndpoint(self.session)
        self.case = CaseEndpoint(self.session)
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

        # connector endpoints
        self.cortex = CortexEndpoint(self.session)

    @property
    def session_organisation(self) -> Optional[str]:
        return self.session.headers.get("X-Organisation")

    @session_organisation.setter
    def session_organisation(self, organisation: Optional[str] = None):
        if organisation:
            self.session.headers["X-Organisation"] = organisation
        else:
            self.session.headers.pop("X-Organisation", None)
