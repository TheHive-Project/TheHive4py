from typing import List

import pytest

from tests.utils import TestConfig
from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.query.filters import Eq
from thehive4py.query.sort import Asc
from thehive4py.types.case import OutputCase
from thehive4py.types.task import InputBulkUpdateTask, InputUpdateTask, OutputTask


class TestTaskEndpoint:
    def test_create_and_get(self, thehive: TheHiveApi, test_case: OutputCase):
        created_task = thehive.task.create(
            case_id=test_case["_id"], task={"title": "test task"}
        )

        fetched_task = thehive.task.get(task_id=created_task["_id"])

        assert created_task == fetched_task

    def test_delete(self, thehive: TheHiveApi, test_task: OutputTask):
        thehive.task.delete(task_id=test_task["_id"])

        with pytest.raises(TheHiveError):
            thehive.task.get(task_id=test_task["_id"])

    def test_update(self, thehive: TheHiveApi, test_task: OutputTask):
        update_fields: InputUpdateTask = {"title": "updated task title"}
        thehive.task.update(task_id=test_task["_id"], fields=update_fields)

        updated_task = thehive.task.get(task_id=test_task["_id"])

        for key, value in update_fields.items():
            assert updated_task.get(key) == value

    def test_bulk_update(self, thehive: TheHiveApi, test_tasks: List[OutputTask]):
        task_ids = [task["_id"] for task in test_tasks]
        update_fields: InputBulkUpdateTask = {
            "ids": task_ids,
            "title": "my updated task",
        }

        thehive.task.bulk_update(fields=update_fields)
        updated_tasks = thehive.task.find()

        expected_fields = {
            key: value for key, value in update_fields.items() if key != "ids"
        }
        for updated_task in updated_tasks:
            for key, value in expected_fields.items():
                assert updated_task.get(key) == value

    def test_set_as_required_and_done(
        self, test_config: TestConfig, thehive: TheHiveApi, test_task: OutputTask
    ):
        organisation = test_config.main_org

        thehive.task.set_as_required(task_id=test_task["_id"], org_id=organisation)
        actions = thehive.task.get_required_actions(task_id=test_task["_id"])
        assert actions[organisation] is True

        thehive.task.set_as_done(task_id=test_task["_id"], org_id=organisation)
        actions = thehive.task.get_required_actions(task_id=test_task["_id"])
        assert actions[organisation] is False

    def test_share_and_unshare(
        self, thehive: TheHiveApi, test_task: OutputTask, test_config: TestConfig
    ):
        thehive.task.share(
            task_id=test_task["_id"], organisations=[test_config.main_org]
        )

        # TODO: test `unshare` once a second organisation is allowed by the license
        # thehive.task.unshare(
        #     task_id=test_task["_id"], organisations=[test_config.main_org]
        # )

        # TODO: test `list_shares` better once a second organisation is
        # allowed by the license
        assert len(thehive.task.list_shares(task_id=test_task["_id"])) == 0

    def test_find_and_count(self, thehive: TheHiveApi, test_tasks: List[OutputTask]):
        filters = Eq("title", test_tasks[0]["title"]) | Eq(
            "title", test_tasks[1]["title"]
        )
        found_tasks = thehive.task.find(
            filters=filters,
            sortby=Asc("_createdAt"),
        )

        task_count = thehive.task.count(filters=filters)

        assert found_tasks == test_tasks
        assert len(test_tasks) == task_count

    def test_create_and_get_logs(self, thehive: TheHiveApi, test_task: OutputTask):
        created_task = thehive.task.create_log(
            task_id=test_task["_id"], task_log={"message": "my test log"}
        )
        task_logs = thehive.task.find_logs(task_id=test_task["_id"])
        assert created_task in task_logs
