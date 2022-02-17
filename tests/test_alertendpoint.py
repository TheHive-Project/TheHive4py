from typing import List

import pytest
from thehive4py.client import TheHiveApi
from thehive4py.query.filters import Eq, Like
from thehive4py.query.sort import Asc
from thehive4py.types.alert import InputAlert, OutputAlert


@pytest.fixture
def test_alert(thehive: TheHiveApi) -> OutputAlert:
    return thehive.alert.create(
        {
            "title": "my first alert",
            "description": "...",
            "type": "test",
            "source": "test",
            "sourceRef": "first",
            "externalLink": "http://",
            "date": 123,
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
        },
        {
            "title": "my second alert",
            "description": "...",
            "type": "test",
            "source": "test",
            "sourceRef": "second",
        },
    ]
    return [thehive.alert.create(alert) for alert in alerts]


class TestAlertEndpoint:
    def test_create_and_get(self, thehive: TheHiveApi):
        created_alert = thehive.alert.create(
            {
                "title": "my first alert",
                "description": "...",
                "type": "test",
                "source": "test",
                "sourceRef": "first",
                "externalLink": "http://",
                "date": 123,
                "tags": ["whatever"],
            }
        )

        fetched_alert = thehive.alert.get(created_alert["_id"])
        assert created_alert == fetched_alert

    def test_update(self, thehive: TheHiveApi, test_alert: OutputAlert):

        alert_id = test_alert["_id"]
        update_fields = {
            "title": "my updated alert",
            "description": "my updated description",
        }
        thehive.alert.update(id_or_name=alert_id, fields=update_fields)
        updated_alert = thehive.alert.get(id_or_name=alert_id)

        assert updated_alert["title"] == update_fields["title"]
        assert updated_alert["description"] == update_fields["description"]

    def test_read_and_unread(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]

        thehive.alert.read(id_or_name=alert_id)
        read_alert = thehive.alert.get(id_or_name=alert_id)
        assert read_alert["read"] is True

        thehive.alert.unread(id_or_name=alert_id)
        read_alert = thehive.alert.get(id_or_name=alert_id)
        assert read_alert["read"] is False

    def test_follow_and_unfollow(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]

        thehive.alert.unfollow(id_or_name=alert_id)
        unfollowed_alert = thehive.alert.get(id_or_name=alert_id)
        assert unfollowed_alert["follow"] is False

        thehive.alert.follow(id_or_name=alert_id)
        followed_alert = thehive.alert.get(id_or_name=alert_id)
        assert followed_alert["follow"] is True

    def test_promote_to_case(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]

        case_from_alert = thehive.alert.promote_to_case(id_or_name=alert_id)
        promoted_alert = thehive.alert.get(id_or_name=alert_id)
        assert promoted_alert["caseId"] == case_from_alert["_id"]

    def test_find_and_count(self, thehive: TheHiveApi, test_alerts: List[OutputAlert]):
        found_alerts = thehive.alert.find(
            filters=Eq("title", test_alerts[0]["title"])
            | Like("title", test_alerts[1]["title"]),
            sortby=Asc("_createdAt"),
        )

        assert found_alerts == test_alerts
