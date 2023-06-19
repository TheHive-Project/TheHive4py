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
    """
    Class representing TheHive's observable type endpoint.

    Parameters:
        - EndpointBase: TheHive4py EndpointBase class.
    """

    def create(self, observable_type: InputObservableType) -> OutputObservableType:
        """
        Creates a new observable type.

        Parameters:
            - observable_type (InputObservableType): An object containing the observable type data.

        Returns:
            - OutputObservableType: An object containing the created observable type data.
        """
        return self._session.make_request(
            "POST", path="/api/v1/observable/type", json=observable_type
        )

    def get(self, observable_type_id: str) -> OutputObservableType:
        """
        Gets the specified observable type.

        Parameters:
            - observable_type_id (str): The ID of the observable type.

        Returns:
            - OutputObservableType: An object containing the observable type data.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/observable/type/{observable_type_id}"
        )

    def delete(self, observable_type_id: str) -> None:
        """
        Deletes the specified observable type.

        Parameters:
            - observable_type_id (str): The ID of the observable type.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/observable/type/{observable_type_id}"
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputObservableType]:
        """
        Gets a list of observable types based on the provided filters, sort expression, and pagination parameters.

        Parameters:
            - filters (Optional[FilterExpr]): A list of filter expressions to filter the returned observable types.
            - sortby (Optional[SortExpr]): A list of sort expressions to sort the returned observable types.
            - paginate (Optional[Paginate]): An object containing pagination data.

        Returns:
            - List[OutputObservableType]: A list of objects containing the observable type data.
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
