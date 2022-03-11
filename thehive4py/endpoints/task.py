from typing import List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.task import (
    InputBulkUpdateTask,
    InputTask,
    InputUpdateTask,
    OutputTask,
)
from thehive4py.types.task_log import InputTaskLog, OutputTaskLog


class TaskEndpoint(EndpointBase):
    def create(self, case_id: str, task: InputTask) -> OutputTask:
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/task", json=task
        )

    def get(self, task_id: str) -> OutputTask:
        return self._session.make_request("GET", path=f"/api/v1/task/{task_id}")

    def delete(self, task_id: str) -> None:
        return self._session.make_request("DELETE", path=f"/api/v1/task/{task_id}")

    def update(self, task_id: str, fields: InputUpdateTask) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/task/{task_id}", json=fields
        )

    def bulk_update(self, fields: InputBulkUpdateTask) -> None:
        return self._session.make_request(
            "PATCH", path="/api/v1/task/_bulk", json=fields
        )

    def get_required_actions(self, task_id: str) -> dict:
        return self._session.make_request(
            "GET", path=f"/api/v1/task/{task_id}/actionRequired"
        )

    def set_as_required(self, task_id: str, org_id: str) -> None:
        return self._session.make_request(
            "PUT", f"/api/v1/task/{task_id}/actionRequired/{org_id}"
        )

    def set_as_done(self, task_id: str, org_id: str) -> None:
        return self._session.make_request(
            "PUT", f"/api/v1/task/{task_id}/actionDone/{org_id}"
        )

    def share(self):
        raise NotImplementedError()

    def list_shares(self):
        raise NotImplementedError()

    def unshare(self):
        raise NotImplementedError()

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputTask]:
        query: QueryExpr = [
            {"_name": "listTask"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "tasks"},
            json={"query": query},
        )

    def count(self, filters: Optional[FilterExpr] = None) -> int:
        query: QueryExpr = [
            {"_name": "listTask"},
            *self._build_subquery(filters=filters),
            {"_name": "count"},
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "task.count"},
            json={"query": query},
        )

    def create_log(self, task_id: str, task_log: InputTaskLog) -> OutputTaskLog:
        return self._session.make_request(
            "POST", path=f"/api/v1/task/{task_id}/log", json=task_log
        )

    def find_logs(
        self,
        task_id: str,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputTaskLog]:
        query: QueryExpr = [
            {"_name": "getTask", "idOrName": task_id},
            {"_name": "logs"},
            *self._build_subquery(filters=filters, sortby=sortby, paginate=paginate),
        ]

        return self._session.make_request(
            "POST",
            path="/api/v1/query",
            params={"name": "case-task-logs"},
            json={"query": query},
        )
