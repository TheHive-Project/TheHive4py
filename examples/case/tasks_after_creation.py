from thehive4py import TheHiveApi
from thehive4py.types.task import InputTask

hive = TheHiveApi(url="thehive.example", apikey="h1v3b33")


case_to_enrich = hive.case.create(
    case={
        "title": "case to enrich",
        "description": "a case to enrich with tasks",
    }
)

case_tasks: list[InputTask] = [
    {"title": "Summarize", "description": "Summarize the investigation"},
    {"title": "Report", "description": "Create a report for the CISO"},
]


for case_task in case_tasks:
    hive.case.create_task(case_id=case_to_enrich["_id"], task=case_task)
