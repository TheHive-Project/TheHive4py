import time
from typing import List

import pytest
from thehive4py.client import TheHiveApi
from thehive4py.types.alert import InputAlert, OutputAlert
from thehive4py.types.case import InputCase, OutputCase
from thehive4py.types.observable import InputObservable, OutputObservable
from thehive4py.types.task import InputTask, OutputTask
from thehive4py.types.task_log import InputTaskLog, OutputTaskLog

from tests.utils import Container, reinit_hive_container, spawn_hive_container


@pytest.fixture(scope="session")
def thehive_container():
    container = spawn_hive_container()
    yield container


@pytest.fixture(scope="function", autouse=True)
def init_hive_container(thehive_container: Container):
    client = TheHiveApi(
        url=thehive_container.url, username="admin@org1.test", password="secret"
    )
    reinit_hive_container(client)


@pytest.fixture(scope="session")
def thehive(thehive_container: Container):
    client = TheHiveApi(
        url=thehive_container.url, username="admin@org1.test", password="secret"
    )
    return client


@pytest.fixture
def test_alert(thehive: TheHiveApi) -> OutputAlert:
    return thehive.alert.create(
        alert={
            "title": "my first alert",
            "description": "...",
            "type": "test",
            "source": "test",
            "sourceRef": "first",
            "externalLink": "http://",
            "date": int(time.time() * 1000),
            "tags": ["whatever"],
        }
    )


@pytest.fixture
def test_alerts(thehive: TheHiveApi) -> List[OutputAlert]:
    alerts: List[InputAlert] = [
        {
            "title": "my first alert",
            "description": "...",
            "type": "test",
            "source": "test",
            "sourceRef": "first",
            "date": int(time.time() * 1000),
        },
        {
            "title": "my second alert",
            "description": "...",
            "type": "test",
            "source": "test",
            "sourceRef": "second",
            "date": int(time.time() * 1000),
        },
    ]
    return [thehive.alert.create(alert=alert) for alert in alerts]


@pytest.fixture
def test_case(thehive: TheHiveApi) -> OutputCase:
    return thehive.case.create(
        case={"title": "my first case", "description": "...", "tags": ["whatever"]}
    )


@pytest.fixture
def test_cases(thehive: TheHiveApi) -> List[OutputCase]:
    cases: List[InputCase] = [
        {"title": "my first case", "description": "...", "tags": ["whatever"]},
        {"title": "my second case", "description": "...", "tags": ["whatever"]},
    ]
    return [thehive.case.create(case=case) for case in cases]


@pytest.fixture
def test_observable(thehive: TheHiveApi, test_case: OutputCase) -> OutputObservable:
    return thehive.observable.create_in_case(
        case_id=test_case["_id"],
        observable={
            "dataType": "domain",
            "data": "example.com",
            "message": "test observable",
            "tlp": 1,
            "pap": 1,
            "tags": ["test-tag"],
        },
    )[0]


@pytest.fixture
def test_observables(
    thehive: TheHiveApi, test_case: OutputCase
) -> List[OutputObservable]:
    observables: List[InputObservable] = [
        {
            "dataType": "domain",
            "data": "example.com",
            "message": "test observable",
            "tlp": 1,
            "pap": 1,
            "tags": ["test-tag"],
        },
        {
            "dataType": "ip",
            "data": "127.0.0.1",
            "message": "test observable",
            "tlp": 2,
            "pap": 2,
            "tags": ["test-tag"],
        },
    ]
    return [
        thehive.observable.create_in_case(
            case_id=test_case["_id"], observable=observable
        )[0]
        for observable in observables
    ]


@pytest.fixture
def test_task(thehive: TheHiveApi, test_case: OutputCase) -> OutputTask:
    return thehive.task.create(
        case_id=test_case["_id"],
        task={"title": "my first task"},
    )


@pytest.fixture
def test_tasks(thehive: TheHiveApi, test_case: OutputCase) -> List[OutputTask]:
    tasks: List[InputTask] = [
        {"title": "my first task"},
        {"title": "my second task"},
    ]
    return [thehive.task.create(case_id=test_case["_id"], task=task) for task in tasks]


@pytest.fixture
def test_task_log(thehive: TheHiveApi, test_task: OutputTask) -> OutputTaskLog:
    return thehive.task_log.create(
        task_id=test_task["_id"],
        task_log={"message": "test log"},
    )


@pytest.fixture
def test_task_logs(thehive: TheHiveApi, test_task: OutputTask) -> List[OutputTaskLog]:
    task_logs: List[InputTaskLog] = [
        {"message": "my first log"},
        {"message": "my second log"},
    ]
    return [
        thehive.task_log.create(task_id=test_task["_id"], task_log=task_log)
        for task_log in task_logs
    ]
