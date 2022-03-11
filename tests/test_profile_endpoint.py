import pytest
from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.query.filters import Eq
from thehive4py.types.profile import InputUpdateProfile, OutputProfile


class TestProfileEndpoint:
    def test_create_and_get(self, thehive_admin: TheHiveApi):
        profile = thehive_admin.profile.create(
            profile={"name": "test-profile", "permissions": []}
        )
        assert profile == thehive_admin.profile.get(profile_id=profile["_id"])

    def test_create_and_delete(
        self, thehive_admin: TheHiveApi, test_profile: OutputProfile
    ):
        thehive_admin.profile.delete(profile_id=test_profile["_id"])

        with pytest.raises(TheHiveError):
            thehive_admin.profile.get(profile_id=test_profile["_id"])

    def test_update(self, thehive_admin: TheHiveApi, test_profile: OutputProfile):
        update_fields: InputUpdateProfile = {
            "name": "updated-test-profile",
            "permissions": ["manageAlert", "manageCase"],
        }
        thehive_admin.profile.update(
            profile_id=test_profile["_id"], fields=update_fields
        )

        updated_profile = thehive_admin.profile.get(profile_id=test_profile["_id"])
        for field, value in update_fields.items():
            assert updated_profile.get(field) == value

    def test_find_and_count(
        self, thehive_admin: TheHiveApi, test_profile: OutputProfile
    ):
        filters = Eq("name", test_profile["name"])
        found_profiles = thehive_admin.profile.find(
            filters=filters,
        )

        profile_count = thehive_admin.profile.count(filters=filters)

        assert test_profile in found_profiles
        assert len(found_profiles) == profile_count
