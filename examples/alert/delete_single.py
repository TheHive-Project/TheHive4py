import uuid

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

alert_to_delete = hive.alert.create(
    alert={
        "type": "delete",
        "source": "tutorial",
        "sourceRef": uuid.uuid4().hex,
        "title": "delete alert",
        "description": "an alert to delete",
    }
)


hive.alert.delete(alert_id=alert_to_delete["_id"])
