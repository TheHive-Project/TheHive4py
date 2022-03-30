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
from thehive4py.types.observable import InputObservable, OutputObservable
from thehive4py.types.share import InputShare, OutputShare
from thehive4py.types.task import InputTask, OutputTask
from thehive4py.types.timeline import OutputTimeline

CaseId = Union[str, int]


class CaseEndpoint(EndpointBase):
    def create(self, case: InputCase) -> OutputCase:
        return self._session.make_request("POST", path="/api/v1/case", json=case)

    def get(self, case_id: CaseId) -> OutputCase:
        return self._session.make_request("GET", path=f"/api/v1/case/{case_id}")

    def delete(self, case_id: CaseId) -> None:
        self._session.make_request("DELETE", path=f"/api/v1/case/{case_id}")

    def update(self, case_id: CaseId, case: InputUpdateCase) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/case/{case_id}", json=case
        )

    def bulk_update(self, fields: InputBulkUpdateCase) -> None:
        return self._session.make_request(
            "PATCH", path="/api/v1/case/_bulk", json=fields
        )

    def merge(self, case_ids: Sequence[CaseId]) -> OutputCase:
        case_id_subpath = ",".join([str(case_id) for case_id in case_ids])
        return self._session.make_request(
            "POST", path=f"/api/v1/case/_merge/{case_id_subpath}"
        )

    def unlink_alert(self, case_id: str, alert_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/{case_id}/alert/{alert_id}"
        )

    def merge_similar_observables(self, case_id: CaseId) -> dict:
        # TODO: add better return value type hint
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/observable/_merge"
        )

    def get_linked_cases(self, case_id: CaseId) -> List[OutputCase]:
        return self._session.make_request("GET", path=f"/api/v1/case/{case_id}/links")

    def delete_custom_field(self, custom_field_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/customField/{custom_field_id}"
        )

    def import_from_file(self, import_case: InputImportCase, import_path: str) -> dict:
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
        return self._session.make_request(
            "GET",
            path=f"/api/v1/case/{case_id}/export",
            params={"password": password},
            download_path=export_path,
        )

    def get_timeline(self, case_id: CaseId) -> OutputTimeline:
        return self._session.make_request("GET", f"/api/v1/case/{case_id}/timeline")

    def add_attachment(
        self, case_id: CaseId, attachment_paths: List[str]
    ) -> List[OutputAttachment]:
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
        return self._session.make_request(
            "GET",
            path=f"/api/v1/case/{case_id}/attachment/{attachment_id}/download",
            download_path=attachment_path,
        )

    def delete_attachment(self, case_id: CaseId, attachment_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/{case_id}/attachment/{attachment_id}"
        )

    def list_shares(self, case_id: CaseId) -> List[OutputShare]:
        return self._session.make_request("GET", path=f"/api/v1/case/{case_id}/shares")

    def share(self, case_id: CaseId, shares: List[InputShare]) -> List[OutputShare]:
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/shares", json={"shares": shares}
        )

    def unshare(self, case_id: CaseId, organisation_ids: List[str]) -> None:
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/case/{case_id}/shares",
            json={"organisations": organisation_ids},
        )

    def set_share(self, case_id: CaseId, shares: List[InputShare]) -> List[OutputShare]:
        return self._session.make_request(
            "PUT", path=f"/api/v1/case/{case_id}/shares", json={"shares": shares}
        )

    def remove_share(self, share_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/case/share/{share_id}"
        )

    def update_share(self, share_id: str, profile: str) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/case/share/{share_id}", json={"profile": profile}
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputCase]:
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

    def find_attachments(
        self,
        case_id: CaseId,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputAttachment]:
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

    def close(
        self,
        case_id: CaseId,
        status: CaseStatusValue,
        summary: str,
        impact_status: ImpactStatusValue = "NotApplicable",
    ) -> None:
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
        case: InputUpdateCase = {"status": status}
        return self.update(case_id, case)
