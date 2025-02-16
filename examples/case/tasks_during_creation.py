from thehive4py import TheHiveApi
from thehive4py.types.task import InputTask

hive = TheHiveApi(url="thehive.example", apikey="h1v3b33")


case_tasks: list[InputTask] = [
    {"title": "Triage", "description": "Conduct the initial investigation"},
    {"title": "Respond", "description": "Execute the required actions"},
]

case_with_tasks = hive.case.create(
    case={
        "title": "case with tasks",
        "description": "a case enriched with tasks",
        "tasks": case_tasks,
    }
)
