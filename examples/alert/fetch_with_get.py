import uuid

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

alert_to_get = hive.alert.create(
    alert={
        "type": "get-single",
        "source": "tutorial",
        "sourceRef": uuid.uuid4().hex,
        "title": "alert to get",
        "description": "a single alert to fetch",
    }
)


fetched_alert = hive.alert.get(alert_id=alert_to_get["_id"])
