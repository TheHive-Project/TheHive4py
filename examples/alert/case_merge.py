import uuid

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")


parent_case = hive.case.create(
    case={"title": "parent case", "description": "a simple parent case"}
)

new_alert = hive.alert.create(
    alert={
        "type": "merge-into-case",
        "source": "tutorial",
        "sourceRef": uuid.uuid4().hex,
        "title": "alert to merge",
        "description": "a single alert to merge into a parent case",
    }
)

updated_parent_case = hive.alert.merge_into_case(
    alert_id=new_alert["_id"], case_id=parent_case["_id"]
)
