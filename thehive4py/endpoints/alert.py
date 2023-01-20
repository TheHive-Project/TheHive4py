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
    def create(
        self, alert: InputAlert, attachment_map: Optional[Dict[str, str]] = None
    ) -> OutputAlert:
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
        return self._session.make_request("GET", path=f"/api/v1/alert/{alert_id}")

    def update(self, alert_id: str, fields: InputUpdateAlert) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/alert/{alert_id}", json=fields
        )

    def delete(self, alert_id: str) -> None:
        return self._session.make_request("DELETE", path=f"/api/v1/alert/{alert_id}")

    def bulk_update(self, fields: InputBulkUpdateAlert) -> None:
        return self._session.make_request(
            "PATCH", path="/api/v1/alert/_bulk", json=fields
        )

    def bulk_delete(self, ids: List[str]) -> None:
        return self._session.make_request(
            "POST", path="/api/v1/alert/delete/_bulk", json={"ids": ids}
        )

    def follow(self, alert_id: str) -> None:
        self._session.make_request("POST", path=f"/api/v1/alert/{alert_id}/follow")

    def unfollow(self, alert_id: str) -> None:
        self._session.make_request("POST", path=f"/api/v1/alert/{alert_id}/unfollow")

    def promote_to_case(
        self, alert_id: str, fields: InputPromoteAlert = {}
    ) -> OutputCase:
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
        kwargs = self._build_observable_kwargs(
            observable=observable, observable_path=observable_path
        )
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/observable", **kwargs
        )

    def merge_into_case(self, alert_id: str, case_id: str) -> OutputCase:
        return self._session.make_request(
            "POST", path=f"/api/v1/alert/{alert_id}/merge/{case_id}"
        )

    def bulk_merge_into_case(self, case_id: str, alert_ids: List[str]) -> OutputCase:
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
