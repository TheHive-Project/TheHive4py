import uuid

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

alert_ids_to_delete = []

for i in range(2):
    alert_to_delete = hive.alert.create(
        alert={
            "type": "delete",
            "source": "tutorial",
            "sourceRef": uuid.uuid4().hex,
            "title": f"delete alert #{i}",
            "description": "an alert to delete",
        }
    )
    alert_ids_to_delete.append(alert_to_delete["_id"])


hive.alert.bulk_delete(ids=alert_ids_to_delete)
