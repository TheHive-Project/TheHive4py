from pathlib import Path
from typing import List

import pytest
from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.query.filters import Eq
from thehive4py.query.sort import Asc
from thehive4py.types.alert import InputBulkUpdateAlert, InputUpdateAlert, OutputAlert
from thehive4py.types.case import OutputCase
from thehive4py.types.observable import InputObservable


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
        update_fields: InputUpdateAlert = {
            "title": "my updated alert",
            "description": "my updated description",
        }
        thehive.alert.update(alert_id=alert_id, fields=update_fields)
        updated_alert = thehive.alert.get(alert_id=alert_id)

        assert updated_alert["title"] == update_fields["title"]
        assert updated_alert["description"] == update_fields["description"]

    def test_bulk_update(self, thehive: TheHiveApi, test_alerts: List[OutputAlert]):

        alert_ids = [alert["_id"] for alert in test_alerts]
        update_fields: InputBulkUpdateAlert = {
            "ids": alert_ids,
            "title": "my updated alert #1",
            "description": "my updated description #1",
        }

        thehive.alert.bulk_update(fields=update_fields)
        updated_alerts = thehive.alert.find()

        for updated_alert in updated_alerts:
            assert updated_alert["title"] == update_fields["title"]
            assert updated_alert["description"] == update_fields["description"]

    def test_follow_and_unfollow(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]

        thehive.alert.unfollow(alert_id=alert_id)
        unfollowed_alert = thehive.alert.get(alert_id=alert_id)
        assert unfollowed_alert["follow"] is False

        thehive.alert.follow(alert_id=alert_id)
        followed_alert = thehive.alert.get(alert_id=alert_id)
        assert followed_alert["follow"] is True

    def test_promote_to_case(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]

        case_from_alert = thehive.alert.promote_to_case(alert_id=alert_id)
        promoted_alert = thehive.alert.get(alert_id=alert_id)
        assert promoted_alert.get("caseId") == case_from_alert["_id"]

    def test_merge_into_case(
        self, thehive: TheHiveApi, test_alert: OutputAlert, test_case: OutputCase
    ):
        alert_id = test_alert["_id"]
        case_id = test_case["_id"]

        merged_case = thehive.alert.merge_into_case(alert_id=alert_id, case_id=case_id)

        merged_alert = thehive.alert.get(alert_id=alert_id)
        assert merged_alert.get("caseId") == merged_case["_id"]

    def test_bulk_merge_into_case(
        self, thehive: TheHiveApi, test_alerts: List[OutputAlert], test_case: OutputCase
    ):
        alert_ids = [alert["_id"] for alert in test_alerts]
        case_id = test_case["_id"]

        merged_case = thehive.alert.bulk_merge_into_case(
            case_id=case_id, alert_ids=alert_ids
        )

        for alert in thehive.alert.find():
            assert alert.get("caseId") == merged_case["_id"]

    def test_find_and_count(self, thehive: TheHiveApi, test_alerts: List[OutputAlert]):
        found_alerts = thehive.alert.find(
            filters=Eq("title", test_alerts[0]["title"])
            | Eq("title", test_alerts[1]["title"]),
            sortby=Asc("_createdAt"),
        )
        alert_count = thehive.alert.count()

        assert found_alerts == test_alerts
        assert len(found_alerts) == alert_count

    def test_delete(self, thehive: TheHiveApi, test_alert: OutputAlert):
        alert_id = test_alert["_id"]
        thehive.alert.delete(alert_id)
        with pytest.raises(TheHiveError):
            thehive.alert.get(alert_id)

    def test_bulk_delete(self, thehive: TheHiveApi, test_alerts: List[OutputAlert]):
        alert_ids = [alert["_id"] for alert in test_alerts]
        thehive.alert.bulk_delete(ids=alert_ids)
        for alert_id in alert_ids:
            with pytest.raises(TheHiveError):
                thehive.alert.get(alert_id)

    def test_create_and_get_observable(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):

        created_observables = thehive.alert.create_observable(
            test_alert["_id"], {"dataType": "domain", "data": "example.com"}
        )
        alert_observables = thehive.alert.find_observables(test_alert["_id"])
        assert created_observables == alert_observables

    def test_create_observable_from_file(
        self, thehive: TheHiveApi, test_alert: OutputAlert, tmp_path: Path
    ):
        observable_path = str(tmp_path / "alert-observable.txt")
        with open(observable_path, "w") as observable_fp:
            observable_fp.write("observable content")

        created_observable = thehive.observable.create_in_alert(
            alert_id=test_alert["_id"],
            observable={
                "dataType": "file",
                "message": "file based observable",
            },
            observable_path=observable_path,
        )[0]

        fetched_observable = thehive.observable.get(
            observable_id=created_observable["_id"]
        )
        assert created_observable == fetched_observable

        attachment = fetched_observable.get("attachment")
        assert attachment and attachment["name"] in observable_path

    def test_create_alert_with_observables(self, thehive: TheHiveApi):
        created_alert = thehive.alert.create(
            {
                "title": "my first alert",
                "description": "...",
                "type": "test",
                "source": "test",
                "sourceRef": "second",
                "externalLink": "http://",
                "date": 123,
                "tags": ["whatever"],
                "observables": [
                    {"dataType": "url", "data": "example.org"},
                    {"dataType": "mail", "data": "foo@example.org"},
                ],
            }
        )

        fetched_alert = thehive.alert.get(created_alert["_id"])
        assert created_alert == fetched_alert
        assert created_alert["observableCount"] == 2

    def test_create_alert_with_observable_file(
        self, thehive: TheHiveApi, tmp_path: Path
    ):
        attachment_path = str(tmp_path / "alert-observable.txt")
        with open(attachment_path, "w") as attachment_fp:
            attachment_fp.write("observable content")

        alert_observables: List[InputObservable] = [
            {"dataType": "url", "data": "example.com"},
            {"dataType": "file", "attachment": "obs1"},
        ]
        created_alert = thehive.alert.create(
            alert={
                "title": "my first alert",
                "description": "...",
                "type": "test",
                "source": "test",
                "sourceRef": "third",
                "date": 123,
                "observables": alert_observables,
            },
            attachment_map={"obs1": attachment_path},
        )
        assert created_alert["observableCount"] == len(alert_observables)
