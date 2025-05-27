import json as jsonlib
import warnings
from typing import Any, Dict, List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.alert import (
    InputAlert,
    InputBulkUpdateAlert,
    InputPromoteAlert,
    InputUpdateAlert,
    OutputAlert,
)
from thehive4py.types.attachment import OutputAttachment
from thehive4py.types.case import OutputCase
from thehive4py.types.comment import OutputComment
from thehive4py.types.observable import InputObservable, OutputObservable
from thehive4py.types.procedure import InputProcedure, OutputProcedure


class AlertEndpoint(EndpointBase):
    def create(
        self, alert: InputAlert, attachment_map: Optional[Dict[str, str]] = None
    ) -> OutputAlert:
        """Create an alert.

        Args:
            alert: The body of the alert.
            attachment_map: An optional mapping of observable attachment keys and paths.

        Returns:
            The created alert.
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
        """Get an alert by id.

        Args:
            alert_id: The id of the alert.

        Returns:
            The alert specified by the id.
        """

        return self._session.make_request("GET", path=f"/api/v1/alert/{alert_id}")

    def delete(self, alert_id: str) -> None:
        """Delete an alert.

        Args:
            alert_id: The id of the alert.

        Returns:
            N/A
        """
        return self._session.make_request("DELETE", path=f"/api/v1/alert/{alert_id}")

    def update(self, alert_id: str, fields: InputUpdateAlert) -> None:
        """Update an alert.

        Args:
            alert_id: The id of the alert.
            fields: The fields of the alert to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/alert/{alert_id}", json=fields
        )

    def bulk_update(self, fields: InputBulkUpdateAlert) -> None:
        """Update multiple alerts with the same values.

        Args:
            fields: The ids and the fields of the alerts to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path="/api/v1/alert/_bulk", json=fields
        )

    def promote_to_case(
        self, alert_id: str, fields: InputPromoteAlert = {}
    ) -> OutputCase:
        """Promote an alert into a case.

        Args:
            alert_id: The id of the alert.
            fields: Override for the fields of the case created from the alert.

        Returns:
            The case from the promoted alert.
        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/alert/{alert_id}/case",
            json=fields,
        )

    def follow(self, alert_id: str) -> None:
        """Follow an alert.

        Args:
            alert_id: The id of the alert.

        Returns:
            N/A
        """
        self._session.make_request("POST", path=f"/api/v1/alert/{alert_id}/follow")

    def unfollow(self, alert_id: str) -> None:
        """Unfollow an alert.

        Args:
            alert_id: The id of the alert.

        Returns:
            N/A
        """
        self._session.make_request("POST", path=f"/api/v1/alert/{alert_id}/unfollow")

    def merge_into_case(self, alert_id: str, case_id: str) -> OutputCase:
        """Merge an alert into an existing case.

        Args:
            alert_id: The id of the alert to merge.
            case_id: The id of the case to merge the alert into.

        Returns:
            The case into which the alert was merged.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/merge/{case_id}"
        )

    def import_into_case(self, alert_id: str, case_id: str) -> OutputCase:
        """Import alert observables and procedures into an existing case.

        Args:
            alert_id: The id of the alert to merge.
            case_id: The id of the case to merge the alert into.

        Returns:
            The case into which the alert observables/procedures were imported.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/import/{case_id}"
        )

    def bulk_merge_into_case(self, case_id: str, alert_ids: List[str]) -> OutputCase:
        """Merge an alert into an existing case.

        Args:
            case_id: The id of the case to merge the alerts into.
            alert_ids: The list of alert ids to merge.

        Returns:
            The case into which the alerts were merged.
        """
        return self._session.make_request(
            "POST",
            path="/api/v1/alert/merge/_bulk",
            json={"caseId": case_id, "alertIds": alert_ids},
        )

    def bulk_delete(self, ids: List[str]) -> None:
        """Delete multiple alerts.

        Args:
            ids: The ids of the alerts to delete.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST", path="/api/v1/alert/delete/_bulk", json={"ids": ids}
        )

    def get_similar_observables(
        self, alert_id: str, alert_or_case_id: str
    ) -> List[OutputObservable]:
        """Get similar observables between an alert and another alert or case.

        Args:
            alert_id: The id of the alert to use as base for observable similarity.
            alert_or_case_id: The id of the alert/case to get similar observables from.

        Returns:
            The list of similar observables.
        """
        return self._session.make_request(
            "GET",
            path=f"/api/v1/alert/{alert_id}/similar/{alert_or_case_id}/observables",
        )

    def add_attachment(
        self,
        alert_id: str,
        attachment_paths: List[str],
        can_rename: bool = True,
    ) -> List[OutputAttachment]:
        """Create an attachment in an alert.

        Args:
            alert_id: The id of the alert.
            attachment_paths: List of paths to the attachments to create.
            can_rename: If set to True, the files can be renamed if they already exist
                with the same name.

        Returns:
            The created alert attachments.
        """
        files = [
            ("attachments", self._fileinfo_from_filepath(attachment_path))
            for attachment_path in attachment_paths
        ]
        return self._session.make_request(
            "POST",
            f"/api/v1/alert/{alert_id}/attachments",
            data={"canRename": can_rename},
            files=files,
        )["attachments"]

    def delete_attachment(self, alert_id: str, attachment_id: str) -> None:
        """Delete an alert attachment.

        Args:
            alert_id: The id of the alert.
            attachment_id: The id of the alert attachment.

        Returns:
            N/A
        """

        return self._session.make_request(
            "DELETE", path=f"/api/v1/alert/{alert_id}/attachment/{attachment_id}"
        )

    def download_attachment(
        self, alert_id: str, attachment_id: str, attachment_path: str
    ) -> None:
        """Download an alert attachment.

        !!! warning
            Deprecated: use [organisation.download_attachment]
            [thehive4py.endpoints.organisation.OrganisationEndpoint.download_attachment]
            instead

        Args:
            alert_id: The id of the alert.
            attachment_id: The id of the alert attachment.
            attachment_path: The local path to download the attachment to.

        Returns:
            N/A
        """

        warnings.warn(
            message=(
                "Deprecated: use the organisation.download_attachment method instead"
            ),
            category=DeprecationWarning,
            stacklevel=2,
        )
        return self._session.make_request(
            "GET",
            path=f"/api/v1/alert/{alert_id}/attachment/{attachment_id}/download",
            download_path=attachment_path,
        )

    def create_observable(
        self,
        alert_id: str,
        observable: InputObservable,
        observable_path: Optional[str] = None,
    ) -> List[OutputObservable]:
        """Create an observable in an alert.

        Args:
            alert_id: The id of the alert.
            observable: The fields of the observable to create.
            observable_path: Optional path in case of a file based observable.

        Returns:
            The created alert observables.
        """

        kwargs = self._build_observable_kwargs(
            observable=observable, observable_path=observable_path
        )
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/observable", **kwargs
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputAlert]:
        """Find multiple alerts.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of alerts matched by the query or an empty list.
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
        """Count alerts.

        Args:
            filters: The filter expressions to apply in the query.

        Returns:
            The count of alerts matched by the query.
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
        """Find observables related to an alert.

        Args:
            alert_id: The id of the alert.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of alert observables matched by the query or an empty list.
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
        """Find comments related to an alert.

        Args:
            alert_id: The id of the alert.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of alert comments matched by the query or an empty list.
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
        """Create an alert procedure.

        Args:
            alert_id: The id of the alert.
            procedure: The fields of the procedure to create.

        Returns:
            The created alert procedure.
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
        """Find procedures related to an alert.

        Args:
            alert_id: The id of the alert.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of alert procedures matched by the query or an empty list.
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

    def find_attachments(
        self,
        alert_id: str,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputAttachment]:
        """Find attachments related to an alert.

        Args:
            alert_id: The id of the alert.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of alert attachments matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "getAlert", "idOrName": alert_id},
            {"_name": "attachments"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "alert-attachments"},
            json={"query": query},
        )
