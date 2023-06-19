from typing import List, Optional, Sequence, Union

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.attachment import OutputAttachment
from thehive4py.types.case import (
    CaseStatus,
    CaseStatusValue,
    ImpactStatusValue,
    InputBulkUpdateCase,
    InputCase,
    InputImportCase,
    InputUpdateCase,
    OutputCase,
)
from thehive4py.types.comment import OutputComment
from thehive4py.types.observable import InputObservable, OutputObservable
from thehive4py.types.procedure import InputProcedure, OutputProcedure
from thehive4py.types.share import InputShare, OutputShare
from thehive4py.types.task import InputTask, OutputTask
from thehive4py.types.timeline import OutputTimeline

CaseId = Union[str, int]


class CaseEndpoint(EndpointBase):
    """
    Provides methods for interacting with TheHive's Case API.

    Parameters:
        - EndpointBase: TheHive4py EndpointBase class.

    """

    def create(self, case: InputCase) -> OutputCase:
        """
        Creates a new case in TheHive.

        Parameters:
            - case (InputCase): The case to create.

        Returns:
            - OutputCase: The created case.
        """
        return self._session.make_request("POST", path="/api/v1/case", json=case)

    def get(self, case_id: CaseId) -> OutputCase:
        """
        Retrieves an existing case from TheHive.

        Parameters:
            - case_id (Union[str, int]): The ID of the case to retrieve.

        Returns:
            - OutputCase: The retrieved case.
        """
        return self._session.make_request("GET", path=f"/api/v1/case/{case_id}")

    def delete(self, case_id: CaseId) -> None:
        """
        Deletes an existing case from TheHive.

        Parameters:
            - case_id (Union[str, int]): The ID of the case to delete.

        Returns:
            None
        """
        self._session.make_request("DELETE", path=f"/api/v1/case/{case_id}")

    def update(self, case_id: CaseId, case: InputUpdateCase) -> None:
        """
        Updates an existing case in TheHive.

        Parameters:
            - case_id (Union[str, int]): The ID of the case to update.
            - case (InputUpdateCase): The updated case.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/case/{case_id}", json=case
        )

    def bulk_update(self, fields: InputBulkUpdateCase) -> None:
        """
        Updates multiple cases in TheHive.

        Parameters:
            - fields (InputBulkUpdateCase): The fields to update.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path="/api/v1/case/_bulk", json=fields
        )

    def merge(self, case_ids: Sequence[CaseId]) -> OutputCase:
        """
        Merges multiple cases into a single case.

        Parameters:
            - case_ids (Sequence[Union[str, int]]): The IDs of the cases to merge.

        Returns:
            - OutputCase: The merged case.
        """
        case_id_subpath = ",".join([str(case_id) for case_id in case_ids])
        return self._session.make_request(
            "POST", path=f"/api/v1/case/_merge/{case_id_subpath}"
        )

    def unlink_alert(self, case_id: str, alert_id: str) -> None:
        """
        Remove a link between a case and an alert.

        Parameters:
            - case_id (str): The ID of the case to unlink the alert from.
            - alert_id (str): The ID of the alert to unlink from the case.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/{case_id}/alert/{alert_id}"
        )

    def merge_similar_observables(self, case_id: CaseId) -> dict:
        """
        Merge similar observables in a case.

        Parameters:
            - case_id (CaseId): The ID of the case to merge similar observables in.

        Returns:
            - dict: A dictionary containing information about the merged observables.
        """

        # TODO: add better return value type hint
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/observable/_merge"
        )

    def get_linked_cases(self, case_id: CaseId) -> List[OutputCase]:
        """
        Get a list of cases linked to the specified case.

        Parameters:
            - case_id (CaseId): The ID of the case to get linked cases for.

        Returns:
            - List[OutputCase]: A list of OutputCase objects representing the linked cases.
        """
        return self._session.make_request("GET", path=f"/api/v1/case/{case_id}/links")

    def delete_custom_field(self, custom_field_id: str) -> None:
        """
        Delete a custom field.

        Parameters:
            - custom_field_id (str): The ID of the custom field to delete.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/customField/{custom_field_id}"
        )

    def import_from_file(self, import_case: InputImportCase, import_path: str) -> dict:
        """
        Import a case from a file.

        Parameters:
            - import_case (InputImportCase): An InputImportCase object representing the case to import.
            - import_path (str): The path to the file to import.

        Returns:
            - dict: A dictionary containing information about the imported case.
        """
        # TODO: add better return type hints
        return self._session.make_request(
            "POST",
            path="/api/v1/case/import",
            data=import_case,
            files={
                "file": self._fileinfo_from_filepath(import_path),
            },
        )

    def export_to_file(self, case_id: CaseId, password: str, export_path: str) -> None:
        """
        Export a case to a file.

        Parameters:
            - case_id (CaseId): The ID of the case to export.
            - password (str): The password to encrypt the exported file with.
            - export_path (str): The path to save the exported file to.

        Returns:
            None
        """
        return self._session.make_request(
            "GET",
            path=f"/api/v1/case/{case_id}/export",
            params={"password": password},
            download_path=export_path,
        )

    def get_timeline(self, case_id: CaseId) -> OutputTimeline:
        """
        Retrieve the timeline of a case.

        Parameters:
            - case_id (CaseId): The ID of the case.

        Returns:
            - OutputTimeline: The timeline of the case.

        """
        return self._session.make_request("GET", f"/api/v1/case/{case_id}/timeline")

    def add_attachment(
        self, case_id: CaseId, attachment_paths: List[str]
    ) -> List[OutputAttachment]:
        """
        Add one or more attachments to a case.

        Parameters:
            - case_id (CaseId): The ID of the case to add the attachments to.
            - attachment_paths (List[str]): A list of file paths for the attachments to add.

        Returns:
            - List[OutputAttachment]: A list of OutputAttachment objects representing the added attachments.

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
        """
        Download an attachment from a case.

        Parameters:
            - case_id (CaseId): The case's id.
            - attachment_id (str): The attachment's id.
            - attachment_path (str): The attachment's path.

        Returns:
            None
        """
        return self._session.make_request(
            "GET",
            path=f"/api/v1/case/{case_id}/attachment/{attachment_id}/download",
            download_path=attachment_path,
        )

    def delete_attachment(self, case_id: CaseId, attachment_id: str) -> None:
        """
        Delete an attachment from a case.

        Parameters:
            - case_id (CaseId): the case's id.
            - attachment_id (str): The attachment's id.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/{case_id}/attachment/{attachment_id}"
        )

    def list_shares(self, case_id: CaseId) -> List[OutputShare]:
        """
        List the shares of the specified case.

        Parameters:
            - case_id (CaseId): The ID of the case to list the shares of.

        Returns:
            - List[OutputShare]: A list of `OutputShare` objects representing the shares of the specified case.
        """
        return self._session.make_request("GET", path=f"/api/v1/case/{case_id}/shares")

    def share(self, case_id: CaseId, shares: List[InputShare]) -> List[OutputShare]:
        """
        Share the specified case with the specified organisations.

        Parameters:
            - case_id (CaseId): The ID of the case to share.
            - shares (List[InputShare]): A list of `InputShare` objects representing the organisations to share the case with.

        Returns:
            - List[OutputShare]: A list of `OutputShare` objects representing the shares that were created by the operation.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/shares", json={"shares": shares}
        )

    def unshare(self, case_id: CaseId, organisation_ids: List[str]) -> None:
        """
        Unshare the specified case from the specified organisations.

        Parameters:
            - case_id (CaseId): The ID of the case to unshare.
            - organisation_ids (List[str]): A list of organisation IDs representing the organisations to unshare the case from.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/case/{case_id}/shares",
            json={"organisations": organisation_ids},
        )

    def set_share(self, case_id: CaseId, shares: List[InputShare]) -> List[OutputShare]:
        """
        Replace the existing shares of the specified case with the specified organisations.

        Parameters:
            - case_id (CaseId): The ID of the case to set the shares of.
            - shares (List[InputShare]): A list of `InputShare` objects representing the organisations to share the case with.

        Returns:
            - List[OutputShare]: A list of `OutputShare` objects representing the shares that were created by the operation.
        """
        return self._session.make_request(
            "PUT", path=f"/api/v1/case/{case_id}/shares", json={"shares": shares}
        )

    def remove_share(self, share_id: str) -> None:
        """
        Remove the specified share.

        Parameters:
            - share_id (str): The ID of the share to remove.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/share/{share_id}"
        )

    def update_share(self, share_id: str, profile: str) -> None:
        """
        Update the profile of a shared case.

        Parameters:
            - share_id (str): The ID of the share to update.
            - profile (str): The new profile to set.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/case/share/{share_id}", json={"profile": profile}
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputCase]:
        """
        Find cases based on the specified filters, sort order, and pagination.

        Parameters:
            - filters (Optional[FilterExpr]): The filters to apply to the query.
            - sortby (Optional[SortExpr]): The sort order to apply to the results.
            - paginate (Optional[Paginate]): The pagination parameters to apply to the query.

        Returns:
            - List[OutputCase]: A list of matching cases.
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
        """
        Count the number of cases that match the specified filters.

        Parameters:
            - filters (Optional[FilterExpr]): The filters to apply to the query.

        Returns:
            - int: The number of matching cases.
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
        """
        Create a new task for the specified case.

        Parameters:
            - case_id (CaseId): The ID of the case to create the task for.
            - task (InputTask): The task to create.

        Returns:
            - OutputTask: The created task.
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
        """
        Find tasks associated with the specified case.

        Parameters:
            - case_id (CaseId): The ID of the case to search for tasks in.
            - filters (Optional[FilterExpr]): Optional filters to apply to the search. Defaults to None.
            - sortby (Optional[SortExpr]): Optional sort criteria to apply to the results. Defaults to None.
            - paginate (Optional[Paginate]): Optional pagination parameters to apply to the results. Defaults to None.

        Returns:
            - List[OutputTask]: A list of tasks associated with the specified case.
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
        """
        Create one or more observables associated with the specified case.

        Parameters:
            - case_id (CaseId): The ID of the case to create observables for.
            - observable (InputObservable): The observable to create.
            - observable_path (Optional[str]): Optional path to a file containing additional data related to the observable.

        Returns:
            - List[OutputObservable]: A list of observables that were created.
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
        """
        Find observables associated with the specified case.

        Parameters:
            - case_id (CaseId): The ID of the case to search for observables in.
            - filters (Optional[FilterExpr]): Optional filters to apply to the search. Defaults to None.
            - sortby (Optional[SortExpr]): Optional sort criteria to apply to the results. Defaults to None.
            - paginate (Optional[Paginate]): Optional pagination parameters to apply to the results. Defaults to None.

        Returns:
            - List[OutputObservable]: A list of observables associated with the specified case.
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
        """
        Create a new procedure associated with the specified case.

        Parameters:
            - case_id (str): The ID of the case to create the procedure for.
            - procedure (InputProcedure): The procedure to create.

        Returns:
            - OutputProcedure: The procedure that was created.
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
        """
        Finds procedures associated with a given case.

        Parameters:
            - case_id (str): The ID of the case to search for procedures.
            - filters (Optional[FilterExpr]): A filter expression to filter the procedures by.
            - sortby (Optional[SortExpr]): A sort expression to sort the procedures by.
            - paginate (Optional[Paginate]): A pagination object to limit and offset the results.

        Returns:
            - List[OutputProcedure]: A list of procedures associated with the given case.
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

    def find_attachments(
        self,
        case_id: CaseId,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputAttachment]:
        """
        Finds attachments associated with a given case.

        Parameters:
            - case_id (CaseId): The ID  of the case to search for attachments.
            - filters (Optional[FilterExpr]): A filter expression to filter the attachments by.
            - sortby (Optional[SortExpr]): A sort expression to sort the attachments by.
            - paginate (Optional[Paginate]): A pagination object to limit and offset the results.

        Returns:
            - List[OutputAttachment]: A list of attachments associated with the given case.
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
        """
        Finds comments associated with a given case.

        Parameters:
            - case_id (CaseId): The ID of the case to search for comments.
            - filters (Optional[FilterExpr]): A filter expression to filter the comments by.
            - sortby (Optional[SortExpr]): A sort expression to sort the comments by.
            - paginate (Optional[Paginate]): A pagination object to limit and offset the results.

        Returns:
            - List[OutputComment]: A list of comments associated with the given case.
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
        """
        Closes a given case.

        Parameters:
            - case_id (CaseId): The ID of the case to close.
            - status (CaseStatusValue): The status of the case after closing.
            - summary (str): A summary of the case.
            - impact_status (ImpactStatusValue): The impact status of the case after closing.

        Returns:
            - None
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
        """
        Opens a given case.

        Parameters:
            - case_id (CaseId): The ID of the case to open.
            - status (CaseStatusValue): The status of the case after opening. Default is CaseStatus.InProgress.

        Returns:
            - None
        """
        case: InputUpdateCase = {"status": status}
        return self.update(case_id, case)
