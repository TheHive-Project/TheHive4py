import pytest
from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.types.custom_field import InputUpdateCustomField, OutputCustomField


class TestCustomeFieldEndpoint:
    def test_create_and_list(self, thehive_admin: TheHiveApi):
        created_custom_field = thehive_admin.custom_field.create(
            custom_field={
                "name": "my-field",
                "displayName": "My Field",
                "description": "...",
                "group": "default",
                "type": "string",
                "options": [],
            }
        )

        custom_fields = thehive_admin.custom_field.list()
        assert created_custom_field in custom_fields

    def test_delete(
        self, thehive_admin: TheHiveApi, test_custom_field: OutputCustomField
    ):
        thehive_admin.custom_field.delete(custom_field_id=test_custom_field["_id"])

        with pytest.raises(TheHiveError):
            thehive_admin.custom_field.delete(custom_field_id=test_custom_field["_id"])

    def test_update(
        self, thehive_admin: TheHiveApi, test_custom_field: OutputCustomField
    ):

        custom_field_id = test_custom_field["_id"]
        update_fields: InputUpdateCustomField = {
            "displayName": "something else ...",
            "type": "float",
        }
        thehive_admin.custom_field.update(
            custom_field_id=custom_field_id, fields=update_fields
        )
        updated_custom_field = [
            cf
            for cf in thehive_admin.custom_field.list()
            if cf["_id"] == custom_field_id
        ][0]

        for key, value in update_fields.items():
            assert updated_custom_field.get(key) == value
