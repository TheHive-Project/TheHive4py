from thehive4py import TheHiveApi
from thehive4py.types.alert import InputAlert

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

input_alert: InputAlert = {
    "type": "advanced",
    "source": "tutorial",
    "sourceRef": "should-be-unique",
    "title": "an advanced alert",
    "description": "a bit more advanced",
    "tags": ["advanced", "example"],
    "severity": 1,
    "caseTemplate": "my-template",
}

output_alert = hive.alert.create(alert=input_alert)
