from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.errors import TheHiveError
from thehive4py.types.task_log import InputTaskLog, InputUpdateTaskLog, OutputTaskLog


class TaskLogEndpoint(EndpointBase):
    def create(self, task_id: str, task_log: InputTaskLog) -> OutputTaskLog:
        return self._session.make_request(
            "POST", path=f"/api/v1/task/{task_id}/log", json=task_log
        )

    def get(self, task_log_id: str) -> OutputTaskLog:
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
        return self._session.make_request("DELETE", path=f"/api/v1/log/{task_log_id}")

    def update(self, task_log_id: str, fields: InputUpdateTaskLog) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/log/{task_log_id}", json=fields
        )

    def add_attachments(self, task_log_id: str, attachment_paths: List[str]) -> None:
        files = [
            ("attachments", self._fileinfo_from_filepath(attachment_path))
            for attachment_path in attachment_paths
        ]
        return self._session.make_request(
            "POST", f"/api/v1/log/{task_log_id}/attachments", files=files
        )

    def delete_attachment(self, task_log_id: str, attachment_id: str) -> None:
        return self._session.make_request(
            "DELETE", f"/api/v1/log/{task_log_id}/attachments/{attachment_id}"
        )
