from thehive4py import TheHiveApi
from thehive4py.types.observable import InputObservable

hive = TheHiveApi(url="thehive.example", apikey="h1v3b33")


case_to_enrich = hive.case.create(
    case={
        "title": "case to enrich",
        "description": "a case to enrich with simple observables",
    }
)


simple_observable: InputObservable = {
    "dataType": "domain",
    "data": "example.com",
}

hive.case.create_observable(
    case_id=case_to_enrich["_id"],
    observable=simple_observable,
)


bulk_observable: InputObservable = {
    "dataType": "domain",
    "data": ["1.example.com", "2.example.com"],
}

hive.case.create_observable(
    case_id=case_to_enrich["_id"],
    observable=bulk_observable,
)

mixed_observables: list[InputObservable] = [
    {"dataType": "ip", "data": "1.2.3.4"},
    {"dataType": "domain", "data": "example.com"},
]


for observable in mixed_observables:
    hive.case.create_observable(
        case_id=case_to_enrich["_id"],
        observable=observable,
    )
