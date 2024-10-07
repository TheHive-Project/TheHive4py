import uuid

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

original_alert = hive.alert.create(
    alert={
        "type": "update-single",
        "source": "tutorial",
        "sourceRef": uuid.uuid4().hex,
        "title": "original alert",
        "description": "a single alert to update",
    }
)


hive.alert.update(
    alert_id=original_alert["_id"],
    fields={
        "title": "updated alert",
        "tags": ["update-single"],
    },
)

updated_alert = hive.alert.get(alert_id=original_alert["_id"])
