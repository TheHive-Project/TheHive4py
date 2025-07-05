from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.observable_type import InputObservableType, OutputObservableType


class ObservableTypeEndpoint(EndpointBase):
    def get(self, observable_type_id: str) -> OutputObservableType:
        """Get an observable type by id.

        Args:
            observable_type_id: The id of the observable type.

        Returns:
            The observable type specified by the id.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/observable/type/{observable_type_id}"
        )

    def delete(self, observable_type_id: str) -> None:
        """Delete an observable type.

        Args:
            observable_type_id: The id of the observable type.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/observable/type/{observable_type_id}"
        )

    def create(self, observable_type: InputObservableType) -> OutputObservableType:
        """Create an observable type.

        Args:
            observable_type: The body of the observable type.

        Returns:
            The created observable type.
        """
        return self._session.make_request(
            "POST", path="/api/v1/observable/type", json=observable_type
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputObservableType]:
        """Find multiple observable types.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination expression to apply in the query.

        Returns:
            The list of observable types matched by the query or an empty list.
        """
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
