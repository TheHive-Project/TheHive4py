from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.types.task_log import InputTaskLog, InputUpdateTaskLog, OutputTaskLog


class TaskLogEndpoint(EndpointBase):
    def create(self, task_id: str, task_log: InputTaskLog) -> OutputTaskLog:
        """
        Creates a new task log for a given task.

        Parameters:
            - task_id (str): The task to create the task log for.
            - task_log (InputTaskLog): The task log to create.

        Returns:
            - OutputTaskLog: The created task log.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/task/{task_id}/log", json=task_log
        )

    def get(self, task_log_id: str) -> OutputTaskLog:
        """
        Retrieves an existing task log.

        Parameters:
            - task_log_id (str): The ID of the task log to retrieve.

        Returns:
            - OutputTaskLog: The retrieved task log.
        """
        # TODO: temp implementation until a dedicated get endpoint
        logs = self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": [{"_name": "getLog", "idOrName": task_log_id}]},
        )

        try:
            return logs[0]
        except IndexError:
            raise TheHiveError("404 - Task Log Not Found")

    def delete(self, task_log_id: str) -> None:
        """
        Deletes an existing task log.

        Parameters:
            - task_log_id (str): The ID of the task log to delete.

        Returns:
            None
        """
        return self._session.make_request("DELETE", path=f"/api/v1/log/{task_log_id}")

    def update(self, task_log_id: str, fields: InputUpdateTaskLog) -> None:
        """
        Updates an existing task log.

        Parameters:
            - task_log_id (str): The ID of the task log to update.
            - fields (InputUpdateTaskLog): The updated task log.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/log/{task_log_id}", json=fields
        )

    def add_attachments(self, task_log_id: str, attachment_paths: List[str]) -> None:
        """
        Add one or more attachments to a task log.

        Parameters:
            - task_log_id (str): The ID of the task log to add the attachments to.
            - attachment_paths (List[str]): A list of file paths for the attachments to add.

        Returns:
            None
        """
        files = [
            ("attachments", self._fileinfo_from_filepath(attachment_path))
            for attachment_path in attachment_paths
        ]
        return self._session.make_request(
            "POST", f"/api/v1/log/{task_log_id}/attachments", files=files
        )

    def delete_attachment(self, task_log_id: str, attachment_id: str) -> None:
        """
        Delete an attachment from a task log.

        Parameters:
            - task_log_id (CaseId): The task log's id.
            - attachment_id (str): The attachment's id.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", f"/api/v1/log/{task_log_id}/attachments/{attachment_id}"
        )
