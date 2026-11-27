from thehive4py.client import TheHiveApi


def test_browser_only_routes_are_not_exposed_on_public_endpoints():
    thehive = TheHiveApi(url="https://thehive.example.com", apikey="token")

    assert not hasattr(thehive.user, "add_temporary_attachment")
    assert not hasattr(thehive.user, "get_avatar")
    assert not hasattr(thehive.user, "set_login")
    assert not hasattr(thehive.organisation, "get_attachment")

    # Attachment downloads remain supported through the dedicated file-download route.
    assert hasattr(thehive.organisation, "download_attachment")
