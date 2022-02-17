from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.task import OutputTask


class TaskEndpoint(EndpointBase):
    def get(self, task_id: str) -> OutputTask:
        return self._session.make_request("GET", path=f"/api/v1/task/{task_id}")

    def delete(self, task_id: str) -> None:
        self._session.make_request("DELETE", path=f"/api/v1/task/{task_id}")

    def find_logs(
        self,
        task_id: str,
        filters: FilterExpr = None,
        sortby: SortExpr = None,
        paginate: Paginate = None,
    ) -> List[dict]:
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
