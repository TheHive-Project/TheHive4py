from pathlib import Path

import pytest

from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.helpers import now_to_ts
from thehive4py.types.task import OutputTask
from thehive4py.types.task_log import InputUpdateTaskLog, OutputTaskLog


class TestTaskLogEndpoint:
    def test_create_and_get(self, thehive: TheHiveApi, test_task: OutputTask):
        created_log = thehive.task_log.create(
            task_id=test_task["_id"],
            task_log={
                "message": "My test log",
                "includeInTimeline": now_to_ts(),
                "startDate": now_to_ts(),
            },
        )

        fetched_log = thehive.task_log.get(task_log_id=created_log["_id"])

        assert created_log == fetched_log

    def test_create_with_attachment(
        self, thehive: TheHiveApi, test_task: OutputTask, tmp_path: Path
    ):
        attachment_paths = [str(tmp_path / f"attachment-{i}.txt") for i in range(2)]

        for path in attachment_paths:
            with open(path, "w") as attachment_fp:
                attachment_fp.write(f"content of {path}")

        log_with_attachment = thehive.task_log.create(
            task_id=test_task["_id"],
            task_log={
                "message": "My test log",
                "includeInTimeline": now_to_ts(),
                "startDate": now_to_ts(),
                "attachments": attachment_paths,
            },
        )

        assert "attachments" in log_with_attachment
        assert len(log_with_attachment["attachments"]) == len(attachment_paths)

    def test_delete(self, thehive: TheHiveApi, test_task_log: OutputTaskLog):
        thehive.task_log.delete(task_log_id=test_task_log["_id"])

        with pytest.raises(TheHiveError):
            thehive.task_log.get(task_log_id=test_task_log["_id"])

    def test_update(self, thehive: TheHiveApi, test_task_log: OutputTask):
        update_fields: InputUpdateTaskLog = {"message": "updated task log message"}
        thehive.task_log.update(task_log_id=test_task_log["_id"], fields=update_fields)

        updated_task_log = thehive.task_log.get(task_log_id=test_task_log["_id"])

        for key, value in update_fields.items():
            assert updated_task_log.get(key) == value

    def test_add_and_delete_attachment(
        self, thehive: TheHiveApi, test_task_log: OutputTaskLog, tmp_path: Path
    ):
        attachment_path = str(tmp_path / "my-attachment.txt")
        with open(attachment_path, "w") as attachment_fp:
            attachment_fp.write("some content...")

        thehive.task_log.add_attachment(
            task_log_id=test_task_log["_id"], attachment_paths=[attachment_path]
        )

        attachments = thehive.task_log.get(task_log_id=test_task_log["_id"]).get(
            "attachments", []
        )

        for attachment in attachments:
            thehive.task_log.delete_attachment(
                task_log_id=test_task_log["_id"], attachment_id=attachment["_id"]
            )

        attachments = thehive.task_log.get(task_log_id=test_task_log["_id"]).get(
            "attachments", []
        )

        assert attachments == []

    def test_add_and_delete_attachments(
        self, thehive: TheHiveApi, test_task_log: OutputTaskLog, tmp_path: Path
    ):
        attachment_path = str(tmp_path / "my-attachment.txt")
        with open(attachment_path, "w") as attachment_fp:
            attachment_fp.write("some content...")

        with pytest.deprecated_call():
            thehive.task_log.add_attachments(
                task_log_id=test_task_log["_id"], attachment_paths=[attachment_path]
            )

        attachments = thehive.task_log.get(task_log_id=test_task_log["_id"]).get(
            "attachments", []
        )

        for attachment in attachments:
            thehive.task_log.delete_attachment(
                task_log_id=test_task_log["_id"], attachment_id=attachment["_id"]
            )

        attachments = thehive.task_log.get(task_log_id=test_task_log["_id"]).get(
            "attachments", []
        )

        assert attachments == []
