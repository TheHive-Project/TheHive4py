from thehive4py.endpoints import (
    AlertEndpoint,
    CaseEndpoint,
    CommentEndpoint,
    ObservableEndpoint,
    ProcedureEndpoint,
    TaskEndpoint,
    TaskLogEndpoint,
    TimelineEndpoint,
    UserEndpoint,
)
from thehive4py.session import TheHiveSession


class TheHiveApi:
    def __init__(
        self,
        url: str,
        apikey: str = None,
        username: str = None,
        password: str = None,
        organisation: str = None,
        verify=None,
    ):
        session = TheHiveSession(
            url=url,
            apikey=apikey,
            username=username,
            password=password,
            organisation=organisation,
            verify=verify,
        )

        # case management endpoints
        self.alert = AlertEndpoint(session)
        self.case = CaseEndpoint(session)
        self.comment = CommentEndpoint(session)
        self.observable = ObservableEndpoint(session)
        self.procedure = ProcedureEndpoint(session)
        self.task = TaskEndpoint(session)
        self.task_log = TaskLogEndpoint(session)
        self.timeline = TimelineEndpoint(session)

        # user management endpoints
        self.user = UserEndpoint(session)
