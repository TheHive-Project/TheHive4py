from thehive4py.endpoints import (
    AlertEndpoint,
    AuditEndpoint,
    CaseEndpoint,
    CortexEndpoint,
    ObservableEndpoint,
    TaskEndpoint,
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

        self.audit = AuditEndpoint(session)
        self.alert = AlertEndpoint(session)
        self.case = CaseEndpoint(session)
        self.observable = ObservableEndpoint(session)
        self.task = TaskEndpoint(session)
        self.user = UserEndpoint(session)

        # connectors
        self.cortex = CortexEndpoint(session)
