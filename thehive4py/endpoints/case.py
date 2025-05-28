import json as jsonlib
import warnings
from typing import List, Optional, Sequence, Union

from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.attachment import OutputAttachment
from thehive4py.types.case import (
    CaseStatus,
    CaseStatusValue,
    ImpactStatusValue,
    InputApplyCaseTemplate,
    InputBulkUpdateCase,
    InputCase,
    InputCaseAccess,
    InputCaseLink,
    InputCaseOwnerOrganisation,
    InputImportCase,
    InputUpdateCase,
    InputURLLink,
    OutputCase,
    OutputCaseLink,
    OutputCaseObservableMerge,
    OutputImportCase,
)
from thehive4py.types.comment import OutputComment
from thehive4py.types.observable import InputObservable, OutputObservable
from thehive4py.types.page import InputCasePage, InputUpdateCasePage, OutputCasePage
from thehive4py.types.procedure import InputProcedure, OutputProcedure
from thehive4py.types.share import InputShare, OutputShare
from thehive4py.types.task import InputTask, OutputTask
from thehive4py.types.timeline import OutputTimeline

CaseId = Union[str, int]


class CaseEndpoint(EndpointBase):
    def create(self, case: InputCase) -> OutputCase:
        """Create a case.

        Args:
            case: The body of the case.

        Returns:
            The created case.
        """
        return self._session.make_request("POST", path="/api/v1/case", json=case)

    def get(self, case_id: CaseId) -> OutputCase:
        """Get a case by id.

        Args:
            case_id: The id of the case.

        Returns:
            The case specified by the id.
        """
        return self._session.make_request("GET", path=f"/api/v1/case/{case_id}")

    def delete(self, case_id: CaseId) -> None:
        """Delete a case.

        Args:
            case_id: The id of the case.

        Returns:
            N/A
        """
        self._session.make_request("DELETE", path=f"/api/v1/case/{case_id}")

    def update(
        self, case_id: CaseId, fields: Optional[InputUpdateCase] = {}, **kwargs
    ) -> None:
        """Update a case.

        Args:
            case_id: The id of the case.
            fields: The fields of the case to update.

        Returns:
            N/A
        """

        if not fields:
            if "case" not in kwargs:
                raise TheHiveError(
                    f"Unrecognized keyword arguments: {list(kwargs.keys())}. "
                    "Please use the `fields` argument to supply case update values."
                )
            warnings.warn(
                message="The `case` argument has been deprecated to follow the same "
                "convention like other update methods. Please use the `fields` "
                "argument to prevent breaking changes in the future.",
                category=DeprecationWarning,
                stacklevel=2,
            )
            fields = kwargs["case"]

        return self._session.make_request(
            "PATCH", path=f"/api/v1/case/{case_id}", json=fields
        )

    def bulk_update(self, fields: InputBulkUpdateCase) -> None:
        """Update multiple cases with the same values.

        Args:
            fields: The ids and the fields of the cases to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path="/api/v1/case/_bulk", json=fields
        )

    def merge(self, case_ids: Sequence[CaseId]) -> OutputCase:
        """Merge multiple cases into one final case.

        Args:
            case_ids: The ids of the cases to merge.

        Returns:
            The merged case.
        """
        case_id_subpath = ",".join([str(case_id) for case_id in case_ids])
        return self._session.make_request(
            "POST", path=f"/api/v1/case/_merge/{case_id_subpath}"
        )

    def unlink_alert(self, case_id: str, alert_id: str) -> None:
        """Unlink an alert from a case.

        Args:
            case_id: The id of the case to unlink the alert from.
            alert_id: The id of the alert to unlink.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/{case_id}/alert/{alert_id}"
        )

    def merge_similar_observables(self, case_id: CaseId) -> OutputCaseObservableMerge:
        """Merge similar observables of a case.

        Args:
            case_id: The id of the case to merge similar observables for.

        Returns:
            The metadata of the observable merge operation.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/observable/_merge"
        )

    def get_linked_cases(self, case_id: CaseId) -> List[OutputCaseLink]:
        """Get other cases linked to a case.

        Args:
            case_id: The id of the case to get linked cases for.

        Returns:
            The list of linked cases.
        """
        return self._session.make_request("GET", path=f"/api/v1/case/{case_id}/links")

    def delete_custom_field(self, custom_field_id: str) -> None:
        """Delete a custom field from a case.

        Args:
            custom_field_id: The id of the specific custom field to delete from a case.

        Retruns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/customField/{custom_field_id}"
        )

    def import_from_file(
        self, import_case: InputImportCase, import_path: str
    ) -> OutputImportCase:
        """Import a case from a .thar archive file.

        Args:
            import_case: The metadata of the case import.
            import_path: The filepath to the .thar archive.

        Returns:
            The metadata of the case import operation.
        """
        return self._session.make_request(
            "POST",
            path="/api/v1/case/import",
            data={"_json": jsonlib.dumps(import_case)},
            files={"file": self._fileinfo_from_filepath(import_path)},
        )

    def export_to_file(self, case_id: CaseId, password: str, export_path: str) -> None:
        """Export a case to a .thar archive file.

        The file can be used to import the case in an other TheHive instance

        Args:
            case_id: The id of the case to export.
            password: The password to encrypt the .thar file with.
            export_path: The filepath to save the case export to.

        Returns:
            N/A
        """
        return self._session.make_request(
            "GET",
            path=f"/api/v1/case/{case_id}/export",
            params={"password": password},
            download_path=export_path,
        )

    def apply_case_template(self, fields: InputApplyCaseTemplate) -> None:
        """Retroactively apply a case template on a case.

        Args:
            fields: The metadata of the case template apply operation.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST", "/api/v1/case/_bulk/caseTemplate", json=fields
        )

    def change_owner_organisation(
        self, case_id: CaseId, fields: InputCaseOwnerOrganisation
    ) -> None:
        """Update the current owner of the case.

        Beware, the current organisation could lose access to the case
        if no profile is set.

        Args:
            case_id: The id of the case.
            fields: The metadata of the case owner organisation.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST", f"/api/v1/case/{case_id}/owner", json=fields
        )

    def manage_access(self, case_id: CaseId, fields: InputCaseAccess) -> None:
        """Make a case private or public and manage the selected users.

        Args:
            case_id: The id of the case.
            fields: The metadata of the case access.
        """
        return self._session.make_request(
            "POST", f"/api/v1/case/{case_id}/access", json=fields
        )

    def get_similar_observables(
        self, case_id: CaseId, alert_or_case_id: str
    ) -> List[OutputObservable]:
        """Get similar observables between a case and another case or alert.

        Args:
            case_id: The id of the case to use as base for observable similarity.
            alert_or_case_id: The id of the alert/case to get similar observables from.

        Returns:
            The list of similar observables.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/case/{case_id}/similar/{alert_or_case_id}/observables"
        )

    def link_case(self, case_id: CaseId, fields: InputCaseLink) -> None:
        """Add link with another case.

        Args:
            case_id: The id of the case to link.
            fields: The metadata of the case link.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST", f"/api/v1/case/{case_id}/link/case/add", json=fields
        )

    def link_url(self, case_id: CaseId, fields: InputURLLink) -> None:
        """Add link with an external URL.

        Args:
            case_id: The id of the case to link.
            fields: The metadata of the URL link.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST", f"/api/v1/case/{case_id}/link/external/add", json=fields
        )

    def delete_case_link(self, case_id: CaseId, fields: InputCaseLink) -> None:
        """Delete link with an another case.

        Args:
            case_id: The id of the case to unlink.
            fields: The metadata of the existing case link.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST", f"/api/v1/case/{case_id}/link/case/remove", json=fields
        )

    def delete_url_link(self, case_id: CaseId, fields: InputURLLink) -> None:
        """Delete link with an external URL.

        Args:
            case_id: The id of the case to unlink.
            fields: The metadata of the existing case link.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST", f"/api/v1/case/{case_id}/link/external/remove", json=fields
        )

    def get_link_types(self) -> List[str]:
        """Get all link types.

        Returns:
            The list of all link types.

        """
        return self._session.make_request("GET", "/api/v1/case/link/types")

    def get_timeline(self, case_id: CaseId) -> OutputTimeline:
        """Get the timeline of a case.

        Args:
            case_id: The id of the case with the timeline.

        Returns:
            The case timeline.
        """
        return self._session.make_request("GET", f"/api/v1/case/{case_id}/timeline")

    def add_attachment(
        self, case_id: CaseId, attachment_paths: List[str]
    ) -> List[OutputAttachment]:
        """Create an attachment in a case.

        Args:
            case_id: The id of the case.
            attachment_paths: List of paths to the attachments to create.

        Returns:
            The created case attachments.
        """

        files = [
            ("attachments", self._fileinfo_from_filepath(attachment_path))
            for attachment_path in attachment_paths
        ]
        return self._session.make_request(
            "POST", f"/api/v1/case/{case_id}/attachments", files=files
        )["attachments"]

    def download_attachment(
        self, case_id: CaseId, attachment_id: str, attachment_path: str
    ) -> None:
        """Download a case attachment.

        !!! warning
            Deprecated: use [organisation.download_attachment]
            [thehive4py.endpoints.organisation.OrganisationEndpoint.download_attachment]
            instead

        Args:
            case_id: The id of the case.
            attachment_id: The id of the case attachment.
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
            path=f"/api/v1/case/{case_id}/attachment/{attachment_id}/download",
            download_path=attachment_path,
        )

    def delete_attachment(self, case_id: CaseId, attachment_id: str) -> None:
        """Delete a case attachment.

        Args:
            case_id: The id of the case.
            attachment_id: The id of the case attachment.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/{case_id}/attachment/{attachment_id}"
        )

    def list_shares(self, case_id: CaseId) -> List[OutputShare]:
        """List all organisation shares of a case.

        Args:
            case_id: The id of the case.

        Returns:
            The list of organisation shares of the case.
        """
        return self._session.make_request("GET", path=f"/api/v1/case/{case_id}/shares")

    def set_share(self, case_id: CaseId, shares: List[InputShare]) -> List[OutputShare]:
        """Set the share for a case with other organisations.

        For each organisation, you can define a profile (level of access) that the org
        will receive. Contrary to `share` this method can delete and update already
        existing shares.

        Args:
            case_id: The id of the case.
            shares: The list of organisational share rules.

        Returns:
            The list of organisation shares of the case.
        """
        return self._session.make_request(
            "PUT", path=f"/api/v1/case/{case_id}/shares", json={"shares": shares}
        )

    def share(self, case_id: CaseId, shares: List[InputShare]) -> List[OutputShare]:
        """Share the case with other organisations.

        For each organisation, you can define a profile (level of access) that the org
        will receive. This method will only create new shares and will not update or
        delete existing shares.

        Args:
            case_id: The id of the case.
            shares: The list of organisational share rules.

        Returns:
            The list of organisation shares of the case.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/shares", json={"shares": shares}
        )

    def unshare(self, case_id: CaseId, organisation_ids: List[str]) -> None:
        """Unshare a case from other organisations.

        Args:
            case_id: The id of the case.
            organisation_ids: The ids of the organisations to unshare from.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/case/{case_id}/shares",
            json={"organisations": organisation_ids},
        )

    def remove_share(self, share_id: str) -> None:
        """Remove a specific organisation share from a case.

        Args:
            share_id: The id of the share to remove.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/share/{share_id}"
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputCase]:
        """Find multiple cases.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of cases matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "listCase"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "cases"},
            json={"query": query},
        )

    def count(self, filters: Optional[FilterExpr] = None) -> int:
        """Count cases.

        Args:
            filters: The filter expressions to apply in the query.

        Returns:
            The count of cases matched by the query.
        """
        query: QueryExpr = [
            {"_name": "listCase"},
            *self._build_subquery(filters=filters),
            {"_name": "count"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "cases.count"},
            json={"query": query},
        )

    def create_task(self, case_id: CaseId, task: InputTask) -> OutputTask:
        """Create a case task.

        Args:
            case_id: The id of the case.
            task: The fields of the task to create.

        Returns:
            The created case task.
        """
        return self._session.make_request(
            "POST",
            path=f"/api/v1/case/{case_id}/task",
            json=task,
        )

    def find_tasks(
        self,
        case_id: CaseId,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputTask]:
        """Find tasks related to a case.

        Args:
            case_id: The id of the case.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of case tasks matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "getCase", "idOrName": case_id},
            {"_name": "tasks"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "case-tasks"},
            json={"query": query},
        )

    def create_observable(
        self,
        case_id: CaseId,
        observable: InputObservable,
        observable_path: Optional[str] = None,
    ) -> List[OutputObservable]:
        """Create an observable in an case.

        Args:
            case_id: The id of the case.
            observable: The fields of the observable to create.
            observable_path: Optional path in case of a file based observable.

        Returns:
            The created case observables.
        """
        kwargs = self._build_observable_kwargs(
            observable=observable, observable_path=observable_path
        )
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/observable", **kwargs
        )

    def find_observables(
        self,
        case_id: CaseId,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputObservable]:
        """Find observables related to a case.

        Args:
            case_id: The id of the case.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of case observables matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "getCase", "idOrName": case_id},
            {"_name": "observables"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "case-observables"},
            json={"query": query},
        )

    def create_procedure(
        self, case_id: str, procedure: InputProcedure
    ) -> OutputProcedure:
        """Create a case procedure.

        Args:
            case_id: The id of the case.
            procedure: The fields of the procedure to create.

        Returns:
            The created case procedure.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/procedure", json=procedure
        )

    def find_procedures(
        self,
        case_id: str,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputProcedure]:
        """Find procedures related to a case.

        Args:
            case_id: The id of the case.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of case procedures matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "getCase", "idOrName": case_id},
            {"_name": "procedures"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "case-procedures"},
            json={"query": query},
        )

    def create_page(self, case_id: str, page: InputCasePage) -> OutputCasePage:
        """Create a page in a case.

        Args:
            case_id: The id of the case.
            page: The fields of the page to create.

        Returns:
            The created case page.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/page", json=page
        )

    def delete_page(self, case_id: str, page_id: str) -> None:
        """Delete a page from a case.

        Args:
            case_id: The id of the case.
            page_id: The id of the page to delete.

        Retruns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/{case_id}/page/{page_id}"
        )

    def update_page(
        self, case_id: str, page_id: str, page: InputUpdateCasePage
    ) -> None:
        """Update a page of a case.

        Args:
            case_id: The id of the case.
            page_id: The id of the page to update.
            page: The fields of the page to update.

        Retruns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/case/{case_id}/page/{page_id}", json=page
        )

    def find_pages(
        self,
        case_id: str,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputProcedure]:
        """Find pages related to a case.

        Args:
            case_id: The id of the case.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of case pages matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "getCase", "idOrName": case_id},
            {"_name": "pages"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "case-pages"},
            json={"query": query},
        )

    def find_attachments(
        self,
        case_id: CaseId,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputAttachment]:
        """Find attachments related to a case.

        Args:
            case_id: The id of the case.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of case attachments matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "getCase", "idOrName": case_id},
            {"_name": "attachments"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "case-attachments"},
            json={"query": query},
        )

    def find_comments(
        self,
        case_id: CaseId,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputComment]:
        """Find comments related to a case.

        Args:
            case_id: The id of the case.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination experssion to apply in the query.

        Returns:
            The list of case comments matched by the query or an empty list.
        """
        query: QueryExpr = [
            {"_name": "getCase", "idOrName": case_id},
            {"_name": "comments"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "case-comments"},
            json={"query": query},
        )

    def close(
        self,
        case_id: CaseId,
        status: CaseStatusValue,
        summary: str,
        impact_status: ImpactStatusValue = "NotApplicable",
    ) -> None:
        """Close a case.

        Args:
            case_id: The id of the case.
            status: The status to close the case with.
            summary: The closure summary of the case.
            impact_status: The impact status of the case.

        Returns:
            N/A
        """
        case: InputUpdateCase = {
            "status": status,
            "impactStatus": impact_status,
            "summary": summary,
        }
        return self.update(
            case_id,
            case,
        )

    def open(
        self, case_id: CaseId, status: CaseStatusValue = CaseStatus.InProgress
    ) -> None:
        """Open a closed case.

        Args:
            case_id: The id of the case.
            status: The status to re-open the case with.

        Returns:
            N/A
        """
        case: InputUpdateCase = {"status": status}
        return self.update(case_id, case)
