from typing import List

import pytest

from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.types.alert import OutputAlert
from thehive4py.types.case import OutputCase
from thehive4py.types.comment import InputUpdateComment, OutputComment


class TestCommentEndpoint:
    def test_create_in_alert_and_get(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):
        created_comment = thehive.comment.create_in_alert(
            alert_id=test_alert["_id"],
            comment={
                "message": "test comment",
            },
        )

        fetched_comment = thehive.comment.get(comment_id=created_comment["_id"])
        assert created_comment == fetched_comment

    def test_create_in_case_and_get(self, thehive: TheHiveApi, test_case: OutputCase):
        created_comment = thehive.comment.create_in_case(
            case_id=test_case["_id"],
            comment={
                "message": "test comment",
            },
        )

        fetched_comment = thehive.comment.get(comment_id=created_comment["_id"])
        assert created_comment == fetched_comment

    def test_delete(self, thehive: TheHiveApi, test_comment: OutputComment):
        comment_id = test_comment["_id"]
        thehive.comment.delete(comment_id=comment_id)
        with pytest.raises(TheHiveError):
            thehive.comment.get(comment_id=comment_id)

    def test_update(self, thehive: TheHiveApi, test_comment: OutputComment):
        comment_id = test_comment["_id"]
        update_fields: InputUpdateComment = {
            "message": "updated comment",
        }
        thehive.comment.update(comment_id=test_comment["_id"], fields=update_fields)
        updated_comment = thehive.comment.get(comment_id=comment_id)

        for key, value in update_fields.items():
            assert updated_comment.get(key) == value

    def test_find(
        self,
        thehive: TheHiveApi,
        test_comments: List[OutputComment],
    ):
        found_comments = thehive.comment.find()
        original_ids = [comment["_id"] for comment in test_comments]
        found_ids = [comment["_id"] for comment in found_comments]
        assert sorted(found_ids) == sorted(original_ids)
