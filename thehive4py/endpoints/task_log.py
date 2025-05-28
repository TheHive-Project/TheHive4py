import json as jsonlib
import warnings
from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.types.task_log import InputTaskLog, InputUpdateTaskLog, OutputTaskLog


class TaskLogEndpoint(EndpointBase):
    def create(
        self,
        task_id: str,
        task_log: InputTaskLog,
    ) -> OutputTaskLog:
        """Create a task log.

        Args:
            task_id: The id of the task to create the log in.
            task_log: The body of the task log.

        Returns:
            The created task_log.
        """
        if "attachments" in task_log:
            files: List[tuple] = [
                ("attachments", self._fileinfo_from_filepath(attachment_path))
                for attachment_path in task_log["attachments"]
            ]
            files.append(("_json", jsonlib.dumps(task_log)))
            kwargs: dict = {"files": files}
        else:
            kwargs = {"json": task_log}
        return self._session.make_request(
            "POST", path=f"/api/v1/task/{task_id}/log", **kwargs
        )

    def delete(self, task_log_id: str) -> None:
        """Delete a task log.

        Args:
            task_log_id: The id of the task log.

        Returns:
            N/A
        """
        return self._session.make_request("DELETE", path=f"/api/v1/log/{task_log_id}")

    def update(self, task_log_id: str, fields: InputUpdateTaskLog) -> None:
        """Update a task log.

        Args:
            task_log_id: The id of the task log.
            fields: The fields of the task log to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/log/{task_log_id}", json=fields
        )

    def add_attachment(self, task_log_id: str, attachment_paths: List[str]) -> None:
        """Add attachments to a task log.

        Args:
            task_log_id: The id of the task log.
            attachment_paths: List of paths to the attachments to create.

        Returns:
            The created task log attachments.
        """
        files = [
            ("attachments", self._fileinfo_from_filepath(attachment_path))
            for attachment_path in attachment_paths
        ]
        return self._session.make_request(
            "POST", f"/api/v1/log/{task_log_id}/attachments", files=files
        )

    def add_attachments(self, task_log_id: str, attachment_paths: List[str]) -> None:
        """Add attachments to a task log.

        !!! warning
            Deprecated: use [task_log.add_attachment]
            [thehive4py.endpoints.task_log.TaskLogEndpoint.add_attachment]
            instead

        Args:
            task_log_id: The id of the task log.
            attachment_paths: List of paths to the attachments to create.

        Returns:
            The created task log attachments.
        """
        warnings.warn(
            message=("Deprecated: use the task_log.add_attachment method instead"),
            category=DeprecationWarning,
            stacklevel=2,
        )
        files = [
            ("attachments", self._fileinfo_from_filepath(attachment_path))
            for attachment_path in attachment_paths
        ]
        return self._session.make_request(
            "POST", f"/api/v1/log/{task_log_id}/attachments", files=files
        )

    def delete_attachment(self, task_log_id: str, attachment_id: str) -> None:
        """Delete a task log attachment.

        Args:
            task_log_id: The id of the task log.
            attachment_id: The id of the task log attachment.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", f"/api/v1/log/{task_log_id}/attachments/{attachment_id}"
        )

    def get(self, task_log_id: str) -> OutputTaskLog:
        """Get a task log by id.

        Args:
            task_log_id: The id of the task log.

        Returns:
            The task log specified by the id.
        """
        # TODO: temp implementation until a dedicated get endpoint [if ever ;)]
        logs = self._session.make_request(
            "POST",
            path="/api/v1/query",
            json={"query": [{"_name": "getLog", "idOrName": task_log_id}]},
        )

        try:
            return logs[0]
        except IndexError:
            raise TheHiveError("404 - Task Log Not Found")
