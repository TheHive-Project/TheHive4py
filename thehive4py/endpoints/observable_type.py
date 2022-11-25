from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.types.observable_type import (
    InputObservableType,
    OutputObservableType,
)
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr


class ObservableTypeEndpoint(EndpointBase):
    def create(self, observable_type: InputObservableType) -> OutputObservableType:
        return self._session.make_request(
            "POST", path="/api/v1/observable/type", json=observable_type
        )

    def get(self, observable_type_id: str) -> OutputObservableType:
        return self._session.make_request(
            "GET", path=f"/api/v1/observable/type/{observable_type_id}"
        )

    def delete(self, observable_type_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/observable/type/{observable_type_id}"
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputObservableType]:
        query: QueryExpr = [
            {"_name": "listObservableType"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "observableTypes"},
            json={"query": query},
        )
