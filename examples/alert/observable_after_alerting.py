import uuid

from thehive4py import TheHiveApi
from thehive4py.types.observable import InputObservable

hive = TheHiveApi(url="thehive.example", apikey="h1v3b33")

alert_to_enrich = hive.alert.create(
    alert={
        "type": "alert-without-observables",
        "source": "example",
        "sourceRef": uuid.uuid4().hex,
        "title": "alert without observables",
        "description": "alert without observables",
    }
)

simple_observable: InputObservable = {
    "dataType": "domain",
    "data": "example.com",
}
hive.alert.create_observable(
    alert_id=alert_to_enrich["_id"],
    observable=simple_observable,
)


bulk_observable: InputObservable = {
    "dataType": "domain",
    "data": ["1.example.com", "2.example.com"],
}
hive.alert.create_observable(
    alert_id=alert_to_enrich["_id"],
    observable=bulk_observable,
)


mixed_observables: list[InputObservable] = [
    {"dataType": "ip", "data": "1.2.3.4"},
    {"dataType": "domain", "data": "example.com"},
]
for observable in mixed_observables:
    hive.alert.create_observable(
        alert_id=alert_to_enrich["_id"],
        observable=observable,
    )
