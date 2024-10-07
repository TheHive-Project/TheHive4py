import uuid

from thehive4py import TheHiveApi
from thehive4py.types.alert import InputAlert
from thehive4py.types.observable import InputObservable

hive = TheHiveApi(url="thehive.example", apikey="h1v3b33")

input_alert: InputAlert = {
    "type": "alert-without-observables",
    "source": "example",
    "sourceRef": uuid.uuid4().hex,
    "title": "alert without observables",
    "description": "alert without observables",
}

output_alert = hive.alert.create(alert=input_alert)


input_observables: list[InputObservable] = [
    {"dataType": "ip", "data": "1.2.3.4"},
    {"dataType": "domain", "data": "example.com"},
]


for input_observable in input_observables:
    hive.alert.create_observable(
        alert_id=output_alert["_id"], observable=input_observable
    )
