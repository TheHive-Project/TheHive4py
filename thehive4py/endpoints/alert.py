from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.alert import InputAlert, OutputAlert
from thehive4py.types.case import OutputCase
from thehive4py.types.observable import InputObservable, OutputObservable


class AlertEndpoint(EndpointBase):
    def create(self, alert: InputAlert) -> OutputAlert:
        return self._session.make_request("POST", path="/api/v1/alert", json=alert)

    def get(self, id_or_name: str) -> OutputAlert:
        return self._session.make_request("GET", path=f"/api/v1/alert/{id_or_name}")

    def update(self, id_or_name: str, fields: dict) -> None:
        # NOTE: the returned custom field format is causing errors during update
        # needs more investigation, for now it is not supported and popped out
        fields.pop("customFields", None)

        self._session.make_request(
            "PATCH", path=f"/api/v1/alert/{id_or_name}", json=fields
        )

    def delete(self, id_or_name: str) -> None:
        # NOTE: no delete route in v1 routes
        self._session.make_request("DELETE", path=f"/api/alert/{id_or_name}")

    def read(self, id_or_name: str) -> None:
        self._session.make_request("POST", path=f"/api/v1/alert/{id_or_name}/read")

    def unread(self, id_or_name: str) -> None:
        self._session.make_request("POST", path=f"/api/v1/alert/{id_or_name}/unread")

    def follow(self, id_or_name: str) -> None:
        self._session.make_request("POST", path=f"/api/v1/alert/{id_or_name}/follow")

    def unfollow(self, id_or_name: str) -> None:
        self._session.make_request("POST", path=f"/api/v1/alert/{id_or_name}/unfollow")

    def promote_to_case(self, id_or_name: str) -> OutputCase:
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{id_or_name}/case"
        )

    def find(
        self,
        filters: FilterExpr = None,
        sortby: SortExpr = None,
        paginate: Paginate = None,
    ) -> List[OutputAlert]:
        query: QueryExpr = [
            {"_name": "listAlert"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "alerts"},
            json={"query": query},
        )

    def count(self, filters: FilterExpr = None) -> int:

        query: QueryExpr = [
            {"_name": "listAlert"},
            *self._build_subquery(filters=filters),
            {"_name": "limitedCount"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "alerts.count"},
            json={"query": query},
        )

    def create_observable(
        self, id_or_name: str, observable: InputObservable
    ) -> OutputObservable:
        # NOTE: the backend return the observable in a list
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{id_or_name}/artifact", json=observable
        )[0]

    def find_observables(
        self,
        id_or_name: str,
        filters: FilterExpr = None,
        sortby: SortExpr = None,
        paginate: Paginate = None,
    ) -> List[OutputObservable]:
        query: QueryExpr = [
            {"_name": "getAlert", "idOrName": id_or_name},
            {"_name": "observables"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "alert-observables"},
            json={"query": query},
        )
