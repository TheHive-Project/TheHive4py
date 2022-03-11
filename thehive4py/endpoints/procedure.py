from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.types.procedure import (
    InputProcedure,
    InputUpdateProcedure,
    OutputProcedure,
)


class ProcedureEndpoint(EndpointBase):
    def create_in_alert(
        self, alert_id: str, procedure: InputProcedure
    ) -> OutputProcedure:
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/procedure", json=procedure
        )

    def create_in_case(
        self, case_id: str, procedure: InputProcedure
    ) -> OutputProcedure:
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/procedure", json=procedure
        )

    def get(self, procedure_id: str) -> OutputProcedure:
        # TODO: temp implementation until a dedicated get endpoint
        procedures = self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": [{"_name": "getProcedure", "idOrName": procedure_id}]},
        )
        try:
            return procedures[0]
        except IndexError:
            raise TheHiveError("404 - Procedure not found")

    def delete(self, procedure_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/procedure/{procedure_id}"
        )

    def update(self, procedure_id: str, fields: InputUpdateProcedure) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/procedure/{procedure_id}", json=fields
        )
