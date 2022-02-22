from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.observable import InputObservable, OutputObservable


class ObservableEndpoint(EndpointBase):
    def create_in_alert(
        self, alert_id: str, observable: InputObservable
    ) -> OutputObservable:
        # NOTE: the backend return the observable in a list
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/artifact", json=observable
        )[0]

    def create_in_case(
        self, case_id: str, observable: InputObservable
    ) -> OutputObservable:
        # NOTE: the backend return the observable in a list
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/observable", json=observable
        )[0]

    def get(self, observable_id: str) -> OutputObservable:
        return self._session.make_request(
            "GET", path=f"/api/v1/observable/{observable_id}"
        )

    def delete(self, observable_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/observable/{observable_id}"
        )

    def update(self, observable_id: str, fields: dict) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/observable/{observable_id}", json=fields
        )

    def update_bulk(self, bulk_fields: List[dict]) -> None:
        return self._session.make_request(
            "PATCH", path="/api/observable/v1/_bulk", json=bulk_fields
        )
