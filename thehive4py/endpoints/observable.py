from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.observable import (
    InputBulkUpdateObservable,
    InputObservable,
    InputUpdateObservable,
    OutputObservable,
)
from thehive4py.types.share import OutputShare


class ObservableEndpoint(EndpointBase):
    def create_in_alert(
        self,
        alert_id: str,
        observable: InputObservable,
        observable_path: Optional[str] = None,
    ) -> List[OutputObservable]:
        kwargs = self._build_observable_kwargs(
            observable=observable, observable_path=observable_path
        )
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/observable", **kwargs
        )

    def create_in_case(
        self,
        case_id: str,
        observable: InputObservable,
        observable_path: Optional[str] = None,
    ) -> List[OutputObservable]:
        kwargs = self._build_observable_kwargs(
            observable=observable, observable_path=observable_path
        )
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/observable", **kwargs
        )

    def get(self, observable_id: str) -> OutputObservable:
        return self._session.make_request(
            "GET", path=f"/api/v1/observable/{observable_id}"
        )

    def delete(self, observable_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/observable/{observable_id}"
        )

    def update(self, observable_id: str, fields: InputUpdateObservable) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/observable/{observable_id}", json=fields
        )

    def bulk_update(self, fields: InputBulkUpdateObservable) -> None:
        return self._session.make_request(
            "PATCH", path="/api/v1/observable/_bulk", json=fields
        )

    def share(self, observable_id: str, organisations: List[str]) -> None:
        return self._session.make_request(
            "POST",
            path=f"/api/v1/observable/{observable_id}/shares",
            json={"organisations": organisations},
        )

    def unshare(self, observable_id: str, organisations: List[str]) -> None:
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/observable/{observable_id}/shares",
            json={"organisations": organisations},
        )

    def list_shares(self, observable_id: str) -> List[OutputShare]:
        return self._session.make_request(
            "GET", path=f"/api/v1/case/{observable_id}/shares"
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputObservable]:
        query: QueryExpr = [
            {"_name": "listObservable"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "observables"},
            json={"query": query},
        )

    def count(self, filters: Optional[FilterExpr] = None) -> int:
        query: QueryExpr = [
            {"_name": "listObservable"},
            *self._build_subquery(filters=filters),
            {"_name": "count"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "observable.count"},
            json={"query": query},
        )
