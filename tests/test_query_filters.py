import pytest

from thehive4py import TheHiveApi
from thehive4py.helpers import now_to_ts
from thehive4py.query.filters import (
    Between,
    Contains,
    EndsWith,
    Eq,
    Gt,
    Gte,
    Has,
    Id,
    In,
    Like,
    Lt,
    Lte,
    Match,
    Ne,
    StartsWith,
)
from thehive4py.types.user import OutputUser


class TestQueryFilters:
    def test_between_contains_has_in(self, thehive: TheHiveApi, test_user: OutputUser):
        assert thehive.user.find(
            filters=Between(field="_createdAt", start=0, end=now_to_ts())
        )
        with pytest.deprecated_call():
            assert thehive.user.find(filters=Contains(field="login"))
        assert thehive.user.find(filters=Has(field="login"))
        assert thehive.user.find(
            filters=In(field="login", values=["...", "xyz", test_user["login"]])
        )

    def test_endswith_startswith(self, thehive: TheHiveApi, test_user: OutputUser):
        assert thehive.user.find(
            filters=EndsWith(field="login", value=test_user["login"])
        )
        assert thehive.user.find(
            filters=StartsWith(field="login", value=test_user["login"])
        )

    def test_eq_ne_id(self, thehive: TheHiveApi, test_user: OutputUser):
        assert thehive.user.find(filters=Eq(field="_id", value=test_user["_id"]))
        assert thehive.user.find(filters=Ne(field="_id", value=test_user["login"]))
        assert thehive.user.find(filters=Id(id=test_user["_id"]))

    def test_gt_gte_lt_lte(self, thehive: TheHiveApi, test_user: OutputUser):
        assert thehive.user.find(filters=Gt(field="_createdAt", value=0))
        assert thehive.user.find(filters=Gte(field="_createdAt", value=0))
        assert thehive.user.find(filters=Lt(field="_createdAt", value=now_to_ts()))
        assert thehive.user.find(filters=Lte(field="_createdAt", value=now_to_ts()))

    def test_like_match(self, thehive: TheHiveApi, test_user: OutputUser):
        assert thehive.user.find(filters=Like(field="login", value=test_user["login"]))
        assert thehive.user.find(filters=Match(field="login", value=test_user["login"]))

    def test_and_or_not(self, thehive: TheHiveApi, test_user: OutputUser):
        assert thehive.user.find(
            filters=Id(id=test_user["_id"])
            & (
                Eq(field="login", value=test_user["login"])
                | Eq(field="login", value="...")
            )
            & ~Eq(field="login", value="...")
        )
