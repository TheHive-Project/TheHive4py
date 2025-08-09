from typing import List

import pytest

from tests.utils import TestConfig, reset_hive_instance, spawn_hive_container
from thehive4py.client import TheHiveApi
from thehive4py.helpers import now_to_ts
from thehive4py.types.alert import InputAlert, OutputAlert
from thehive4py.types.case import InputCase, OutputCase
from thehive4py.types.case_template import InputCaseTemplate, OutputCaseTemplate
from thehive4py.types.comment import InputComment, OutputComment
from thehive4py.types.custom_field import OutputCustomField
from thehive4py.types.observable import InputObservable, OutputObservable
from thehive4py.types.observable_type import OutputObservableType
from thehive4py.types.page import OutputCasePage
from thehive4py.types.page_template import InputPageTemplate, OutputPageTemplate
from thehive4py.types.procedure import OutputProcedure
from thehive4py.types.profile import OutputProfile
from thehive4py.types.task import InputTask, OutputTask
from thehive4py.types.task_log import InputTaskLog, OutputTaskLog
from thehive4py.types.timeline import OutputCustomEvent
from thehive4py.types.user import OutputUser


@pytest.fixture(scope="session")
def test_config():
    return TestConfig(
        image_name="strangebee/thehive:5.5.7",
        container_name="thehive4py-integration-tester",
        user="admin@thehive.local",
        password="secret",
        admin_org="admin",
        main_org="main-org",
        share_org="share-org",
    )


@pytest.fixture(scope="function", autouse=True)
def auto_reset_hive_instance(thehive: TheHiveApi, test_config: TestConfig):
    reset_hive_instance(hive_url=thehive.session.hive_url, test_config=test_config)


@pytest.fixture(scope="session")
def thehive(test_config: TestConfig):
    hive_url = spawn_hive_container(test_config=test_config)
    client = TheHiveApi(
        url=hive_url,
        username=test_config.user,
        password=test_config.password,
        organisation=test_config.main_org,
    )
    return client


@pytest.fixture
def thehive_admin(test_config: TestConfig, thehive: TheHiveApi):
    default_organisation = thehive.session_organisation
    thehive.session_organisation = test_config.admin_org
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
def test_case_template(thehive: TheHiveApi) -> OutputCaseTemplate:
    name = "my first case template"
    return thehive.case_template.create(
        case_template={
            "name": name,
            "description": "...",
            "tags": ["template-tag"],
        }
    )


@pytest.fixture
def test_case_templates(thehive: TheHiveApi) -> List[OutputCaseTemplate]:
    case_templates: List[InputCaseTemplate] = [
        {
            "name": "my first case template",
            "description": "...",
            "tags": ["template-tag-1"],
        },
        {
            "name": "my second case template",
            "description": "...",
            "tags": ["template-tag-2"],
        },
    ]
    return [
        thehive.case_template.create(case_template=case_template)
        for case_template in case_templates
    ]


@pytest.fixture
def test_page_template(thehive: TheHiveApi) -> OutputPageTemplate:
    return thehive.page_template.create(
        page_template={
            "title": "my first page template",
            "category": "testing",
            "content": "...",
        }
    )


@pytest.fixture
def test_page_templates(thehive: TheHiveApi) -> List[OutputPageTemplate]:
    page_templates: List[InputPageTemplate] = [
        {
            "title": "my first page template",
            "category": "testing",
            "content": "...",
        },
        {
            "title": "my second case template",
            "category": "testing",
            "content": "...",
        },
    ]
    return [
        thehive.page_template.create(page_template=page_template)
        for page_template in page_templates
    ]


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
def test_comments(thehive: TheHiveApi, test_case: OutputCase) -> List[OutputComment]:
    comments: List[InputComment] = [
        {"message": "my first comment"},
        {"message": "my second comment"},
    ]
    return [
        thehive.comment.create_in_case(case_id=test_case["_id"], comment=comment)
        for comment in comments
    ]


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
def test_case_page(thehive: TheHiveApi, test_case: OutputCase) -> OutputCasePage:
    return thehive.case.create_page(
        case_id=test_case["_id"],
        page={
            "title": "my case page",
            "category": "testing",
            "content": "...",
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
def test_user(test_config: TestConfig, thehive: TheHiveApi) -> OutputUser:
    return thehive.user.create(
        user={
            "email": "user@example.com",
            "name": "test user",
            "login": "user@example.com",
            "profile": "analyst",
            "organisation": test_config.main_org,
        }
    )


@pytest.fixture
def test_profile(thehive_admin: TheHiveApi) -> OutputProfile:
    return thehive_admin.profile.create(
        profile={"name": "my-read-only", "permissions": []}
    )


@pytest.fixture
def test_custom_field(thehive_admin: TheHiveApi) -> OutputCustomField:
    return thehive_admin.custom_field.create(
        custom_field={
            "name": "test-field",
            "type": "string",
            "displayName": "Test Field",
            "description": "...",
            "group": "default",
            "options": [],
        }
    )


@pytest.fixture
def test_observable_type(thehive_admin: TheHiveApi) -> OutputObservableType:
    return thehive_admin.observable_type.create(
        observable_type={"name": "my-observable-type"}
    )
