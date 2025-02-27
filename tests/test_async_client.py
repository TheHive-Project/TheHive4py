"""Test cases for the async TheHive client."""

import pytest

from thehive4py.async_api import TheHiveAsyncApi
from thehive4py.query.filters import Eq
from thehive4py.types.alert import OutputAlert


pytestmark = pytest.mark.asyncio


class TestAsyncClient:
    async def test_get_alert(
        self, async_client: TheHiveAsyncApi, test_alert: OutputAlert
    ):
        """Test async retrieval of an alert."""
        alert = await async_client.alert.get(test_alert["_id"])
        assert alert["_id"] == test_alert["_id"]
        assert alert["title"] == test_alert["title"]

    async def test_session_reuse(
        self, async_client: TheHiveAsyncApi, test_alert: OutputAlert
    ):
        """Test session reuse for multiple requests."""
        async with async_client.session.session_context():
            # First request
            alert = await async_client.alert.get(test_alert["_id"])
            assert alert["_id"] == test_alert["_id"]

            new_title = "Updated Alert"
            # Second request using same session
            await async_client.alert.update(
                alert_id=test_alert["_id"], fields={"title": new_title}
            )

            updated_alert = await async_client.alert.get(test_alert["_id"])
            assert updated_alert["title"] == new_title

    async def test_find_with_filter(
        self, async_client: TheHiveAsyncApi, test_alert: OutputAlert
    ):
        """Test async filtering with query builders."""
        alerts = await async_client.alert.find(filters=Eq("_id", test_alert["_id"]))
        assert len(alerts) == 1
        assert alerts[0]["_id"] == test_alert["_id"]

    async def test_organisation_switch(
        self, async_client: TheHiveAsyncApi, test_config
    ):
        """Test async organisation switching."""
        async_client.session_organisation = test_config.admin_org
        assert async_client.session_organisation == test_config.admin_org

        async_client.session_organisation = test_config.main_org
        assert async_client.session_organisation == test_config.main_org
