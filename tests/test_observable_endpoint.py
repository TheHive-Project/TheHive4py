from pathlib import Path
from typing import List

import pytest
from thehive4py import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.query.sort import Asc
from thehive4py.types.alert import OutputAlert
from thehive4py.types.case import OutputCase
from thehive4py.types.observable import (
    InputBulkUpdateObservable,
    InputUpdateObservable,
    OutputObservable,
)


class TestObservableEndpoint:
    def test_create_in_alert_and_get(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):
        created_observable = thehive.observable.create_in_alert(
            alert_id=test_alert["_id"],
            observable={
                "dataType": "domain",
                "data": "example.com",
                "message": "test observable",
            },
        )[0]

        fetched_observable = thehive.observable.get(
            observable_id=created_observable["_id"]
        )
        assert created_observable == fetched_observable

    def test_create_in_alert_from_file(
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

    def test_create_in_case_and_get(self, thehive: TheHiveApi, test_case: OutputCase):
        created_observable = thehive.observable.create_in_case(
            case_id=test_case["_id"],
            observable={
                "dataType": "domain",
                "data": "example.com",
                "message": "test observable",
            },
        )[0]

        fetched_observable = thehive.observable.get(
            observable_id=created_observable["_id"]
        )
        assert created_observable == fetched_observable

    def test_create_in_case_from_file(
        self, thehive: TheHiveApi, test_case: OutputCase, tmp_path: Path
    ):
        observable_path = str(tmp_path / "case-observable.txt")
        with open(observable_path, "w") as observable_fp:
            observable_fp.write("observable content")

        created_observable = thehive.observable.create_in_case(
            case_id=test_case["_id"],
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

    def test_delete(self, thehive: TheHiveApi, test_observable: OutputObservable):
        observable_id = test_observable["_id"]
        thehive.observable.delete(observable_id=observable_id)
        with pytest.raises(TheHiveError):
            thehive.observable.get(observable_id=observable_id)

    def test_update(self, thehive: TheHiveApi, test_observable: OutputObservable):

        observable_id = test_observable["_id"]
        update_fields: InputUpdateObservable = {
            "dataType": "fqdn",
            "message": "updated observable",
        }
        thehive.observable.update(
            observable_id=test_observable["_id"], fields=update_fields
        )
        updated_observable = thehive.observable.get(observable_id=observable_id)

        for key, value in update_fields.items():
            assert updated_observable.get(key) == value

    def test_bulk_update(
        self, thehive: TheHiveApi, test_observables: List[OutputObservable]
    ):

        observable_ids = [observable["_id"] for observable in test_observables]
        update_fields: InputBulkUpdateObservable = {
            "ids": observable_ids,
            "dataType": "other",
            "message": "updated observable",
        }

        thehive.observable.bulk_update(fields=update_fields)
        updated_observables = thehive.observable.find()

        expected_fields = {
            key: value for key, value in update_fields.items() if key != "ids"
        }
        for updated_task in updated_observables:
            for key, value in expected_fields.items():
                assert updated_task.get(key) == value

    @pytest.mark.skip(
        reason="documentation is unclear and implementation might be changed"
    )
    def test_share_and_unshare(
        self, thehive: TheHiveApi, test_observable: OutputObservable
    ):
        organisation = "share-org"

        thehive.observable.share(
            observable_id=test_observable["_id"], organisations=[organisation]
        )
        assert (
            len(thehive.observable.list_shares(observable_id=test_observable["_id"]))
            == 1
        )

        thehive.observable.unshare(
            observable_id=test_observable["_id"], organisations=[organisation]
        )
        assert (
            len(thehive.observable.list_shares(observable_id=test_observable["_id"]))
            == 0
        )

    def test_find_and_count(
        self, thehive: TheHiveApi, test_observables: List[OutputObservable]
    ):
        found_observables = thehive.observable.find(
            sortby=Asc("_createdAt"),
        )
        observable_count = thehive.observable.count()

        assert found_observables == test_observables
        assert len(test_observables) == observable_count
