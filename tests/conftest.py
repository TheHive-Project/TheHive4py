from typing import List

import pytest
from thehive4py.client import TheHiveApi
from thehive4py.helpers import now_to_ts
from thehive4py.types.alert import InputAlert, OutputAlert
from thehive4py.types.case import InputCase, OutputCase
from thehive4py.types.comment import OutputComment
from thehive4py.types.observable import InputObservable, OutputObservable
from thehive4py.types.procedure import OutputProcedure
from thehive4py.types.profile import OutputProfile
from thehive4py.types.task import InputTask, OutputTask
from thehive4py.types.task_log import InputTaskLog, OutputTaskLog
from thehive4py.types.timeline import OutputCustomEvent
from thehive4py.types.user import OutputUser

from tests.utils import reinit_hive_container, spawn_hive_container


@pytest.fixture(scope="function", autouse=True)
def init_hive_container(thehive: TheHiveApi):
    reinit_hive_container(thehive)


@pytest.fixture(scope="function")
def thehive():
    hive_container = spawn_hive_container()
    client = TheHiveApi(
        url=hive_container.url,
        username="admin@thehive.local",
        password="secret",
        organisation="test-org",
    )
    return client


@pytest.fixture
def thehive_admin(thehive: TheHiveApi):
    default_organisation = thehive.session_organisation
    thehive.session_organisation = "admin"
    yield thehive
    thehive.session_organisation = default_organisation


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
            "date": now_to_ts(),
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
            "date": now_to_ts(),
        },
        {
            "title": "my second alert",
            "description": "...",
            "type": "test",
            "source": "test",
            "sourceRef": "second",
            "date": now_to_ts(),
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


@pytest.fixture
def test_comment(thehive: TheHiveApi, test_case: OutputCase) -> OutputComment:
    return thehive.comment.create_in_case(
        case_id=test_case["_id"],
        comment={"message": "my first comment"},
    )


@pytest.fixture
def test_procedure(thehive: TheHiveApi, test_case: OutputCase) -> OutputProcedure:
    return thehive.procedure.create_in_case(
        case_id=test_case["_id"],
        procedure={
            "occurDate": now_to_ts(),
            "patternId": "T1059.006",
            "tactic": "execution",
            "description": "...",
        },
    )


@pytest.fixture
def test_timeline_event(
    thehive: TheHiveApi, test_case: OutputCase
) -> OutputCustomEvent:
    return thehive.timeline.create_event(
        case_id=test_case["_id"],
        event={
            "date": now_to_ts(),
            "endDate": now_to_ts(),
            "title": "test timeline event",
            "description": "...",
        },
    )


@pytest.fixture
def test_user(thehive: TheHiveApi) -> OutputUser:
    return thehive.user.create(
        user={
            "email": "user@example.com",
            "name": "test user",
            "login": "user@example.com",
            "profile": "analyst",
            "organisation": "test-org",
        }
    )


@pytest.fixture
def test_profile(thehive_admin: TheHiveApi) -> OutputProfile:
    return thehive_admin.profile.create(
        profile={"name": "my-read-only", "permissions": []}
    )
