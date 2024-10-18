import uuid

from thehive4py import TheHiveApi
from thehive4py.types.alert import InputAlert

hive = TheHiveApi(url="thehive.example", apikey="h1v3b33")

input_alert: InputAlert = {
    "type": "alert-with-observables",
    "source": "example",
    "sourceRef": uuid.uuid4().hex,
    "title": "alert with observables",
    "description": "alert with observables",
    "observables": [
        {"dataType": "ip", "data": "1.2.3.4"},
        {"dataType": "domain", "data": "example.com"},
    ],
}

hive.alert.create(alert=input_alert)
