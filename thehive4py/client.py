from thehive4py.endpoints import (
    AlertEndpoint,
    CaseEndpoint,
    CommentEndpoint,
    ObservableEndpoint,
    TaskEndpoint,
    TaskLogEndpoint,
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
        self.task = TaskEndpoint(session)
        self.task_log = TaskLogEndpoint(session)

        # user management endpoints
        self.user = UserEndpoint(session)
