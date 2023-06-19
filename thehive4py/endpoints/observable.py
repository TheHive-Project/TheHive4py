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
        """
        Create an observable within an alert.

        Parameters:
            - alert_id (str): The ID of the alert to create the observable within.
            - observable (InputObservable): The observable to create.
            - observable_path (Optional[str]): The path to the observable file (if it's a file).

        Returns:
            - List[OutputObservable]: A list containing the created observable.
        """
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
        """
        Create an observable within a case.

        Parameters:
            - alert_id (str): The ID of the case to create the observable within.
            - observable (InputObservable): The observable to create.
            - observable_path (Optional[str]): The path to the observable file (if it's a file).

        Returns:
            - List[OutputObservable]: A list containing the created observable.
        """
        kwargs = self._build_observable_kwargs(
            observable=observable, observable_path=observable_path
        )
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/observable", **kwargs
        )

    def get(self, observable_id: str) -> OutputObservable:
        """
        Get information about a specific observable.

        Patrameters:
            - observable_id (str): The ID of the observable to retrieve.

        Returns:
            - OutputObservable: Information about the observable.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/observable/{observable_id}"
        )

    def delete(self, observable_id: str) -> None:
        """
        Delete a specific observable.

        Parameters:
            observable_id (str): The ID of the observable to delete.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/observable/{observable_id}"
        )

    def update(self, observable_id: str, fields: InputUpdateObservable) -> None:
        """
        Update a specific observable.

        Parameters:
            - observable_id (str): The ID of the observable to update.
            - fields (InputUpdateObservable): The fields to update.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/observable/{observable_id}", json=fields
        )

    def bulk_update(self, fields: InputBulkUpdateObservable) -> None:
        """
        Update multiple observables at once.

        Parameters:
            - fields (InputBulkUpdateObservable): The fields to update for the observables.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path="/api/v1/observable/_bulk", json=fields
        )

    def share(self, observable_id: str, organisations: List[str]) -> None:
        """
        Share an observable with a list of organisations.

        Parameters:
            - observable_id (str): The ID of the observable to share.
            - organisations (List[str]): The list of organisations to share the observable with.

        Returns:
            None
        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/observable/{observable_id}/shares",
            json={"organisations": organisations},
        )

    def unshare(self, observable_id: str, organisations: List[str]) -> None:
        """
        Unshare an observable with a list of organisations.

        Parameters:
            - observable_id (str): The ID of the observable to unshare.
            - organisations (List[str]): The list of organisations to unshare the observable with.
        Returns:
            None
        """
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/observable/{observable_id}/shares",
            json={"organisations": organisations},
        )

    def list_shares(self, observable_id: str) -> List[OutputShare]:
        """
        List the organisations with which an observable is shared.

        Parameters:
            - observable_id (str): The ID of the observable to list shares for.

        Returns:
            - List[OutputShare]: A list of share objects for the observable.
        """

        return self._session.make_request(
            "GET", path=f"/api/v1/case/{observable_id}/shares"
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputObservable]:
        """
        Find observables matching the specified criteria.

        Parameters:
        Parameters:
            - filters (Optional[FilterExpr]): The filters to apply to the query.
            - sortby (Optional[SortExpr]): The sort order to apply to the results.
            - paginate (Optional[Paginate]): The pagination parameters to apply to the query.

        Returns:
            - List[OutputObservable]: A list of observables matching the specified criteria.
        """
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
        """
        Count the number of observables matching the specified criteria.

        Parameters:
            - filters (Optional[FilterExpr]): The filter criteria to apply to the search.

        Returns:
            - int: The number of observables matching the specified criteria.
        """
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

    def download_attachment(
        self,
        observable_id: str,
        attachment_id: str,
        observable_path: str,
        as_zip=False,
    ) -> None:

        """
        Downloads an attachment associated with a given observable.

        Parameters:
            - observable_id (str): The ID of the observable that the attachment belongs to.
            - attachment_id (str): The ID of the attachment to download.
            - observable_path (str): The path to save the downloaded attachment to.
            - as_zip (bool, optional): If True, downloads the attachment as a zip file.
        Returns:
            None

        """

        return self._session.make_request(
            "GET",
            path=(
                f"/api/v1/observable/{observable_id}"
                f"/attachment/{attachment_id}/download"
            ),
            params={"asZip": as_zip},
            download_path=observable_path,
        )
