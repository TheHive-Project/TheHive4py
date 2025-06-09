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
    def create_in_case(
        self,
        case_id: str,
        observable: InputObservable,
        observable_path: Optional[str] = None,
    ) -> List[OutputObservable]:
        """Create one or more observables in a case.

        Args:
            case_id: The id of the case.
            observable: The fields of the observable to create.
            observable_path: Optional path in case of file based observables.

        Returns:
            The created case observables.
        """
        kwargs = self._build_observable_kwargs(
            observable=observable, observable_path=observable_path
        )
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/observable", **kwargs
        )

    def create_in_alert(
        self,
        alert_id: str,
        observable: InputObservable,
        observable_path: Optional[str] = None,
    ) -> List[OutputObservable]:
        """Create one or more observables in an alert.

        Args:
            alert_id: The id of the alert.
            observable: The fields of the observable to create.
            observable_path: Optional path in case of file based observables.

        Returns:
            The created alert observables.
        """
        kwargs = self._build_observable_kwargs(
            observable=observable, observable_path=observable_path
        )
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/observable", **kwargs
        )

    def get(self, observable_id: str) -> OutputObservable:
        """Get an observable by id.

        Args:
            observable_id: The id of the observable.

        Returns:
            The observable specified by the id.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/observable/{observable_id}"
        )

    def delete(self, observable_id: str) -> None:
        """Delete an observable.

        Args:
            observable_id: The id of the observable.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/observable/{observable_id}"
        )

    def update(self, observable_id: str, fields: InputUpdateObservable) -> None:
        """Update an observable.

        Args:
            observable_id: The id of the observable.
            fields: The fields of the observable to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/observable/{observable_id}", json=fields
        )

    def bulk_update(self, fields: InputBulkUpdateObservable) -> None:
        """Update multiple observables with the same values.

        Args:
            fields: The ids and the fields of the observables to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path="/api/v1/observable/_bulk", json=fields
        )

    def download_attachment(
        self,
        observable_id: str,
        attachment_id: str,
        observable_path: str,
        as_zip: bool = False,
    ) -> None:
        """Download an observable attachment.

        Args:
            observable_id: The id of the observable.
            attachment_id: The id of the observable attachment.
            observable_path: The local path to download the observable attachment to.
            as_zip: If `True`, the attachment will be sent as a zip file with a
                password. Default password is 'malware'

        Returns:
            N/A
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

    def list_shares(self, observable_id: str) -> List[OutputShare]:
        """List all organisation shares of an observable.

        Args:
            observable_id: The id of the observable.

        Returns:
            The list of organisation shares of the observable.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/case/{observable_id}/shares"
        )

    def share(self, observable_id: str, organisations: List[str]) -> None:
        """Share the observable with other organisations.

        The case that owns the observable must already be shared with the target
        organisations.

        Args:
            observable_id: The id of the observable.
            organisations: The list of organisation names or ids.

        Returns:
            The list of organisation shares of the observable.
        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/observable/{observable_id}/shares",
            json={"organisations": organisations},
        )

    def unshare(self, observable_id: str, organisations: List[str]) -> None:
        """Unshare an observable from other organisations.

        Args:
            observable_id: The id of the observable.
            organisations: The list of organisation names or ids.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/observable/{observable_id}/shares",
            json={"organisations": organisations},
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputObservable]:
        """Find multiple observables.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of observables matched by the query or an empty list.
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
        """Count observables.

        Args:
            filters: The filter expressions to apply in the query.

        Returns:
            The count of observables matched by the query.
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
