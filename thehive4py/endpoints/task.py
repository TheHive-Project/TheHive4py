from typing import Dict, List, Optional

from thehive4py.endpoints._base import EndpointBase
from thehive4py.query import QueryExpr
from thehive4py.query.filters import FilterExpr
from thehive4py.query.page import Paginate
from thehive4py.query.sort import SortExpr
from thehive4py.types.share import OutputShare
from thehive4py.types.task import (
    InputBulkUpdateTask,
    InputTask,
    InputUpdateTask,
    OutputTask,
)
from thehive4py.types.task_log import InputTaskLog, OutputTaskLog


class TaskEndpoint(EndpointBase):
    def create(self, case_id: str, task: InputTask) -> OutputTask:
        """Create a task.

        Args:
            case_id: The id of the case to create the task for.
            task: The body of the task.

        Returns:
            The created task.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/task", json=task
        )

    def get(self, task_id: str) -> OutputTask:
        """Get a task by id.

        Args:
            task_id: The id of the task.

        Returns:
            The task specified by the id.
        """
        return self._session.make_request("GET", path=f"/api/v1/task/{task_id}")

    def delete(self, task_id: str) -> None:
        """Delete a task.

        Args:
            task_id: The id of the task.

        Returns:
            N/A
        """
        return self._session.make_request("DELETE", path=f"/api/v1/task/{task_id}")

    def update(self, task_id: str, fields: InputUpdateTask) -> None:
        """Update a task.

        Args:
            task_id: The id of the task.
            fields: The fields of the task to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/task/{task_id}", json=fields
        )

    def bulk_update(self, fields: InputBulkUpdateTask) -> None:
        """Update multiple tasks with the same values.

        Args:
            fields: The ids and the fields of the tasks to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path="/api/v1/task/_bulk", json=fields
        )

    def get_required_actions(self, task_id: str) -> Dict[str, bool]:
        """Get the required actions per organization for a specific task.

        Args:
            task_id: The id of the task.

        Returns:
            A dictionary where the keys are organization ids and the values are
            booleans indicating whether the task is required for that organization.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/task/{task_id}/actionRequired"
        )

    def set_as_required(self, task_id: str, org_id: str) -> None:
        """Set a task as required.

        Args:
            task_id: The id of the task.
            org_id: The id of the organization where the task is required.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PUT", f"/api/v1/task/{task_id}/actionRequired/{org_id}"
        )

    def set_as_done(self, task_id: str, org_id: str) -> None:
        """Set a task as done.
        Args:
            task_id: The id of the task.
            org_id: The id of the organization where the task is done.
        Returns:
            N/A
        """
        return self._session.make_request(
            "PUT", f"/api/v1/task/{task_id}/actionDone/{org_id}"
        )

    def list_shares(self, task_id: str) -> List[OutputShare]:
        """List the shares of a task.

        Args:
            task_id: The id of the task.

        Returns:
            A list of shares associated with the task.
        """
        return self._session.make_request("GET", f"/api/v1/task/{task_id}/shares")

    def share(self, task_id: str, organisations: List[str]) -> None:
        """Share the task with other organisations.

        The case that owns the observable must already be shared with the
        target organisations.

        Args:
            task_id: The id of the task to share.
            organisations: The list of organisation ids or names.

        Returns:
            N/A
        """
        return self._session.make_request(
            "POST",
            f"/api/v1/task/{task_id}/shares",
            json={"organisations": organisations},
        )

    def unshare(self, task_id: str, organisations: List[str]) -> None:
        """Unshare the task with other organisations.

        Args:
            task_id: The id of the task to unshare.
            organisations: The list of organisation ids or names.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE",
            f"/api/v1/task/{task_id}/shares",
            json={"organisations": organisations},
        )

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputTask]:
        """Find multiple tasks.

        Args:
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination expression to apply in the query.

        Returns:
            The list of tasks matched by the query or an empty list.
        """
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
        """Count tasks.

        Args:
            filters: The filter expressions to apply in the query.

        Returns:
            The count of tasks matched by the query.
        """
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
        """Create a task log.

        Args:
            task_id: The id of the task to create the log for.
            task_log: The body of the task log.
        Returns:
            The created task log.
        """
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
        """Find task logs.

        Args:
            task_id: The id of the task to find logs for.
            filters: The filter expressions to apply in the query.
            sortby: The sort expressions to apply in the query.
            paginate: The pagination expression to apply in the query.

        Returns:
            The list of task logs matched by the query or an empty list.
        """
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
