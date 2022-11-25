import pytest
from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.query.filters import Eq
from thehive4py.types.observable_type import OutputObservableType


class TestObservableTypeEndpoint:
    def test_create_and_get(self, thehive_admin: TheHiveApi):
        created_observable_type = thehive_admin.observable_type.create(
            {
                "name": "new-observable-type",
            }
        )

        test_observable_type = thehive_admin.observable_type.get(
            created_observable_type["_id"]
        )
        assert created_observable_type == test_observable_type

    def test_find(
        self, thehive: TheHiveApi, test_observable_type: OutputObservableType
    ):
        found_observable_types = thehive.observable_type.find(
            filters=Eq("name", test_observable_type["name"])
        )

        assert found_observable_types == [test_observable_type]

    def test_delete(
        self, thehive: TheHiveApi, test_observable_type: OutputObservableType
    ):
        observable_type_id = test_observable_type["_id"]
        thehive.observable_type.delete(observable_type_id)
        with pytest.raises(TheHiveError):
            thehive.observable_type.get(observable_type_id)
