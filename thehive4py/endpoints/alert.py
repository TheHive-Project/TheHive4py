import json as jsonlib
from typing import Any, Dict, List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.alert import (
    InputAlert,
    InputBulkUpdateAlert,
    InputUpdateAlert,
    InputPromoteAlert,
    OutputAlert,
)
from thehive4py.types.case import OutputCase
from thehive4py.types.comment import OutputComment
from thehive4py.types.observable import InputObservable, OutputObservable
from thehive4py.types.procedure import InputProcedure, OutputProcedure


class AlertEndpoint(EndpointBase):
    """
    This class implements TheHive's Alert APIs.

    The Alert APIs are used to interact with TheHive's alerts.

    parameters:
        - EndpointBase: TheHive4py EndpointBase class.

    """

    def create(
        self, alert: InputAlert, attachment_map: Optional[Dict[str, str]] = None
    ) -> OutputAlert:
        """
        Create a new alert.

        Parameters:
            - alert (InputAlert): The data for the new alert.
            - attachment_map (Optional[Dict[str, str]]): A dictionary mapping attachment keys to file paths.

        Returns:
            - OutputAlert: The created alert.
        """
        if attachment_map:
            files: Dict[str, Any] = {
                key: self._fileinfo_from_filepath(path)
                for key, path in attachment_map.items()
            }
            files["_json"] = jsonlib.dumps(alert)
            kwargs: dict = {"files": files}
        else:
            kwargs = {"json": alert}
        return self._session.make_request("POST", path="/api/v1/alert", **kwargs)

    def get(self, alert_id: str) -> OutputAlert:
        """
        Get an existing alert.

        Parameters:
            - alert_id (str): The ID of the alert to get.

        Returns:
            - OutputAlert: The retrieved alert.

        """
        return self._session.make_request("GET", path=f"/api/v1/alert/{alert_id}")

    def update(self, alert_id: str, fields: InputUpdateAlert) -> None:
        """
        Update an existing alert.

        Parameters:
            - alert_id (str): The ID of the alert to update.
            - fields (InputUpdateAlert): The fields to update.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/alert/{alert_id}", json=fields
        )

    def delete(self, alert_id: str) -> None:
        """
        Delete an existing alert.

        Parameters:
            - alert_id (str): The ID of the alert to delete.

        Returns:
            None
        """
        return self._session.make_request("DELETE", path=f"/api/v1/alert/{alert_id}")

    def bulk_update(self, fields: InputBulkUpdateAlert) -> None:
        """
        Update multiple alerts at once.

        Parameters:
            - fields (InputBulkUpdateAlert): The updates to apply.

        Returns:
            None

        """
        return self._session.make_request(
            "PATCH", path="/api/v1/alert/_bulk", json=fields
        )

    def bulk_delete(self, ids: List[str]) -> None:
        """
        Delete multiple alerts at once.

        Parameters:
            - ids (List[str]): The IDs of the alerts to delete.

        Returns:
            None

        """

        return self._session.make_request(
            "POST", path="/api/v1/alert/delete/_bulk", json={"ids": ids}
        )

    def follow(self, alert_id: str) -> None:
        """
        Follow an alert.

        Parameters:
            - alert_id (str): The ID of the alert to follow.

        Returns:
            None

        """
        self._session.make_request("POST", path=f"/api/v1/alert/{alert_id}/follow")

    def unfollow(self, alert_id: str) -> None:
        """
        Unfollow an alert.

        Parameters:
            - alert_id (str): The ID of the alert to unfollow.

        Returns:
            None

        """
        self._session.make_request("POST", path=f"/api/v1/alert/{alert_id}/unfollow")

    def promote_to_case(
        self, alert_id: str, fields: InputPromoteAlert = {}
    ) -> OutputCase:
        """
        Promote an alert to a case.

        Parameters:
            - alert_id (str): The ID of the alert to promote.
            - fields (InputPromoteAlert): The fields to include in the new case.

        Returns:
            - OutputCase: The newly created case.

        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/alert/{alert_id}/case",
            json=fields,
        )

    def create_observable(
        self,
        alert_id: str,
        observable: InputObservable,
        observable_path: Optional[str] = None,
    ) -> List[OutputObservable]:
        """
        Create a new observable associated with the given alert.

        Parameters:
            - alert_id (str): The ID of the alert to associate the observable with.
            - observable (InputObservable): The observable to create.
            - observable_path (str, optional): The path to associate with the observable.

        Returns:
            - List[OutputObservable]: The created observable.

        """
        kwargs = self._build_observable_kwargs(
            observable=observable, observable_path=observable_path
        )
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/observable", **kwargs
        )

    def merge_into_case(self, alert_id: str, case_id: str) -> OutputCase:
        """
        Merge an alert into a case.

        Parameters:
            - alert_id (str): The ID of the alert to merge into the case.
            - case_id (str): The ID of the case to merge the alert into.

        Returns:
            - OutputCase: The updated case.

        """

        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/merge/{case_id}"
        )

    def bulk_merge_into_case(self, case_id: str, alert_ids: List[str]) -> OutputCase:
        """
        Bulk merge alerts into a case.

        Parameters:
            - case_id (str): The ID of the case to merge the alerts into.
            - alert_ids (List[str]): The IDs of the alerts to merge.

        Returns:
            - OutputCase: The updated case.

        """
        return self._session.make_request(
            "POST",
            path="/api/v1/alert/merge/_bulk",
            json={"caseId": case_id, "alertIds": alert_ids},
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputAlert]:
        """
        Find alerts matching the given filters.

        Parameters:
            - filters (FilterExpr, optional): The filters to apply to the search.
            - sortby (SortExpr, optional): The sorting criteria to apply to the search.
            - paginate (Paginate, optional): The pagination settings to apply to the search.

        Returns:
            - List[OutputAlert]: The matching alerts.

        """
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

    def count(self, filters: Optional[FilterExpr] = None) -> int:
        """
        Count alerts matching the given filters.

        Parameters:
            - filters (FilterExpr, optional): The filters to apply to the search.

        Returns:
            - int: The number of matching alerts.
        """
        query: QueryExpr = [
            {"_name": "listAlert"},
            *self._build_subquery(filters=filters),
            {"_name": "count"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "alerts.count"},
            json={"query": query},
        )

    def find_observables(
        self,
        alert_id: str,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputObservable]:
        """
        Find observables associated with the given alert.

        Parameters:
            - alert_id (str): The ID of the alert to retrieve observables for.
            - filters (FilterExpr, optional): The filters to apply to the search.
            - sortby (SortExpr, optional): The sorting criteria to apply to the search.
            - paginate (Paginate, optional): The pagination settings to apply to the search.

        Returns:
            - List[OutputObservable]: The matching observables.

        """
        query: QueryExpr = [
            {"_name": "getAlert", "idOrName": alert_id},
            {"_name": "observables"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "alert-observables"},
            json={"query": query},
        )

    def find_comments(
        self,
        alert_id: str,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputComment]:
        """
        Retrieve comments for a given alert.

        Parameters:
            - alert_id (str): The ID or name of the alert to retrieve comments for.
            - filters (Optional[FilterExpr]): Filters to apply to the comments. Default is None.
            - sortby (Optional[SortExpr]): Sorting to apply to the comments. Default is None.
            - paginate (Optional[Paginate]): Pagination parameters for the comments. Default is None.

        Returns:
            - List[OutputComment]: A list of comments for the given alert.
        """

        query: QueryExpr = [
            {"_name": "getAlert", "idOrName": alert_id},
            {"_name": "comments"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "alert-comments"},
            json={"query": query},
        )

    def create_procedure(
        self, alert_id: str, procedure: InputProcedure
    ) -> OutputProcedure:
        """
        Create a procedure for a given alert.

        Parameters:
            - alert_id (str): The ID or name of the alert to create the procedure for.
            - procedure (InputProcedure): The procedure to create.

        Returns:
            - OutputProcedure: The created procedure.
        """

        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/procedure", json=procedure
        )

    def find_procedures(
        self,
        alert_id: str,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputProcedure]:
        """
        Retrieve procedures for a given alert.

        Parameters:
            - alert_id (str): The ID or name of the alert to retrieve procedures for.
            - filters (Optional[FilterExpr]): Filters to apply to the procedures. Default is None.
            - sortby (Optional[SortExpr]): Sorting to apply to the procedures. Default is None.
            - paginate (Optional[Paginate]): Pagination parameters for the procedures. Default is None.

        Returns:
            - List[OutputProcedure]: A list of procedures for the given alert.
        """

        query: QueryExpr = [
            {"_name": "getAlert", "idOrName": alert_id},
            {"_name": "procedures"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "alert-procedures"},
            json={"query": query},
        )
