import uuid

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

original_alert_ids = []
for i in range(2):
    original_alert = hive.alert.create(
        alert={
            "type": "update-bulk",
            "source": "tutorial",
            "sourceRef": uuid.uuid4().hex,
            "title": f"original alert #{i}",
            "description": "an alert to update in bulk",
        }
    )

    original_alert_ids.append(original_alert["_id"])


hive.alert.bulk_update(
    fields={
        "ids": original_alert_ids,
        "title": "bulk updated alert",
        "tags": ["update-bulk"],
    },
)
