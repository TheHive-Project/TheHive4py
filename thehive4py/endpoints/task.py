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
        """
        Creates a new task in a given case.

        Parameters:
            - case_id (str): The case to create the task within.
            - task (InputTask): The task to create.

        Returns:
            - OutputTask: The created task.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/task", json=task
        )

    def get(self, task_id: str) -> OutputTask:
        """
        Retrieves an existing task.

        Parameters:
            - task_id (str): The ID of the task to retrieve.

        Returns:
            - OutputTask: The retrieved task.
        """
        return self._session.make_request("GET", path=f"/api/v1/task/{task_id}")

    def delete(self, task_id: str) -> None:
        """
        Deletes an existing task.

        Parameters:
            - task_id (str): The ID of the task to delete.

        Returns:
            None
        """
        return self._session.make_request("DELETE", path=f"/api/v1/task/{task_id}")

    def update(self, task_id: str, fields: InputUpdateTask) -> None:
        """
        Updates an existing task.

        Parameters:
            - task_id (str): The ID of the task to update.
            - fields (InputUpdateTask): The task to update.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/task/{task_id}", json=fields
        )

    def bulk_update(self, fields: InputBulkUpdateTask) -> None:
        """
        Updates multiple tasks.

        Parameters:
            - fields (InputBulkUpdateTask): The fields to update.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path="/api/v1/task/_bulk", json=fields
        )

    def get_required_actions(self, task_id: str) -> dict:
        """
        Retrieves the required actions for a specific task.

        Parameters:
            - task_id (str): The ID of the task to retrieve required actions for.

        Returns:
            - dict: A dictionary containing information about the required actions for the task.
        """
        return self._session.make_request(
            "GET", path=f"/api/v1/task/{task_id}/actionRequired"
        )

    def set_as_required(self, task_id: str, org_id: str) -> None:
        """
        Set an organization as required to take action for a specific task.

        Parameters:
            - task_id (str): The ID of the task to set the organization as required for.
            - org_id (str): The ID of the organisation to set as required for the task.

        Returns:
            None
        """
        return self._session.make_request(
            "PUT", f"/api/v1/task/{task_id}/actionRequired/{org_id}"
        )

    def set_as_done(self, task_id: str, org_id: str) -> None:
        """
        Mark an organisation's required action for a specific task as done.

        Parameters:
            - task_id (str): The ID of the task to mark the organization's action as done for.
            - org_id (str): The ID of the organization to mark the action as done for.

        Returns:
            None
        """
        return self._session.make_request(
            "PUT", f"/api/v1/task/{task_id}/actionDone/{org_id}"
        )

    def share(self):
        """
        Share the current object with another user or users.

        Raises:
            NotImplementedError: This method is not implemented yet.
        """
        raise NotImplementedError()

    def list_shares(self):
        """
        List the users or groups with whom the current object has been shared.

        Raises:
            NotImplementedError: This method is not implemented yet.
        """
        raise NotImplementedError()

    def unshare(self):
        """
        Remove any shares of the current object with other users or groups.

        Raises:
            NotImplementedError: This method is not implemented yet.
        """
        raise NotImplementedError()

    def find(
        self,
        filters: Optional[FilterExpr] = None,
        sortby: Optional[SortExpr] = None,
        paginate: Optional[Paginate] = None,
    ) -> List[OutputTask]:
        """
        Find tasks based on the specified filters, sort order, and pagination.

        Parameters:
            - filters (Optional[FilterExpr]): The filters to apply to the query.
            - sortby (Optional[SortExpr]): The sort order to apply to the results.
            - paginate (Optional[Paginate]): The pagination parameters to apply to the query.

        Returns:
            - List[OutputTask]: A list of matching tasks.
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
        """
        Count the number of tasks that match the specified filters.

        Parameters:
            - filters (Optional[FilterExpr]): The filters to apply to the query.

        Returns:
            - int: The number of matching tasks.
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
        """
        Creates a new task log.

        Parameters:
            - task_id (str): The task to create the task log for.
            - task_log (InputTaskLog): The task log to create.

        Returns:
            - OutputTaskLog: The created task log.
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
        """
        Find task logs based on the specified filters, sort order, and pagination.

        Parameters:
            - task_id (str): The ID of the task to retrieve the logs for.
            - filters (Optional[FilterExpr]): The filters to apply to the query.
            - sortby (Optional[SortExpr]): The sort order to apply to the results.
            - paginate (Optional[Paginate]): The pagination parameters to apply to the query.

        Returns:
            - List[OutputTaskLog]: A list of matching task logs.
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
