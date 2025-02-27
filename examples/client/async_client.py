from thehive4py.async_api import TheHiveAsyncApi


async def main():
    # Create client
    client = TheHiveAsyncApi(
        url="http://localhost:9000",
        apikey="h1v3b33",
    )

    # For multiple sequential requests, use session_context()
    async with client.session.session_context():
        alert = await client.alert.get("alert-123")
        await client.alert.update(alert["_id"], {"status": "New"})
