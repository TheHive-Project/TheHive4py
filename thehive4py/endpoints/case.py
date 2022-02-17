from typing import List, Union

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.case import (
    CaseStatus,
    ImpactStatusValue,
    InputCase,
    OutputCase,
    ResolutionStatusValue,
)
from thehive4py.types.observable import InputObservable, OutputObservable
from thehive4py.types.task import InputTask, OutputTask

IdOrName = Union[str, int]


class CaseEndpoint(EndpointBase):
    def create(self, case: InputCase) -> OutputCase:
        return self._session.make_request("POST", path="/api/v1/case", json=case)

    def get(self, id_or_name: IdOrName) -> OutputCase:
        return self._session.make_request("GET", path=f"/api/v1/case/{id_or_name}")

    def update(self, id_or_name: IdOrName, fields: dict) -> None:
        # NOTE: the returned custom field format is causing errors during update
        # needs more investigation, for now it is not supported and popped out
        fields.pop("customFields", None)

        self._session.make_request(
            "PATCH", path=f"/api/v1/case/{id_or_name}", json=fields
        )

    def delete(self, id_or_name: IdOrName) -> None:
        self._session.make_request("DELETE", path=f"/api/v1/case/{id_or_name}")

    def merge(self, *ids_or_names: IdOrName) -> OutputCase:
        id_or_name_subpath = ",".join([str(id_) for id_ in ids_or_names])
        return self._session.make_request(
            "POST", path=f"/api/v1/case/_merge/{id_or_name_subpath}"
        )

    def close(
        self,
        id_or_name: IdOrName,
        resolution: ResolutionStatusValue,
        summary: str,
        impact_status: ImpactStatusValue = "NotApplicable",
    ) -> None:
        case = {
            "status": CaseStatus.Resolved,
            "summary": summary,
            "resolutionStatus": resolution,
            "impactStatus": impact_status,
        }
        return self.update(
            id_or_name,
            case,
        )

    def open(self, id_or_name: IdOrName) -> None:
        case = {"status": CaseStatus.Open}
        return self.update(id_or_name, case)

    def find(
        self,
        filters: FilterExpr = None,
        sortby: SortExpr = None,
        paginate: Paginate = None,
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

    def count(self, filters: FilterExpr = None) -> int:
        query: QueryExpr = [
            {"_name": "listCase"},
            *self._build_subquery(filters=filters),
            {"_name": "limitedCount"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "cases.count"},
            json={"query": query},
        )

    def create_task(self, id_or_name: IdOrName, task: InputTask) -> OutputTask:
        return self._session.make_request(
            "POST", path="/api/v1/task", json={**task, "caseId": id_or_name}
        )[0]

    def find_tasks(
        self,
        id_or_name: IdOrName,
        filters: FilterExpr = None,
        sortby: SortExpr = None,
        paginate: Paginate = None,
    ) -> List[OutputTask]:
        query: QueryExpr = [
            {"_name": "getCase", "idOrName": id_or_name},
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
        self, id_or_name: IdOrName, observable: InputObservable
    ) -> OutputObservable:
        # NOTE: the backend return the observable in a list
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{id_or_name}/observable", json=observable
        )[0]

    def find_observables(
        self,
        id_or_name: IdOrName,
        filters: FilterExpr = None,
        sortby: SortExpr = None,
        paginate: Paginate = None,
    ) -> List[OutputObservable]:
        query: QueryExpr = [
            {"_name": "getCase", "idOrName": id_or_name},
            {"_name": "observables"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]
        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "case-observables"},
            json={"query": query},
        )
