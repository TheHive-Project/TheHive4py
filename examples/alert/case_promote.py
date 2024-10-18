import uuid

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

alert_to_promote = hive.alert.create(
    alert={
        "type": "promote",
        "source": "tutorial",
        "sourceRef": uuid.uuid4().hex,
        "title": "promote to case",
        "description": "an alert to promote to case",
    }
)

case_from_alert = hive.alert.promote_to_case(alert_id=alert_to_promote["_id"])
