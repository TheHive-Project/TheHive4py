from thehive4py import TheHiveApi
from thehive4py.types.page import InputCasePage

hive = TheHiveApi(url="thehive.example", apikey="h1v3b33")


case_pages: list[InputCasePage] = [
    {
        "title": "Notes",
        "category": "default",
        "content": "Some notes to take during case triage.",
    },
    {
        "title": "Summary",
        "category": "default",
        "content": "Some summary to wrap up the case triage.",
    },
]

case_with_tasks = hive.case.create(
    case={
        "title": "case with tasks",
        "description": "a case enriched with tasks",
        "pages": case_pages,
    }
)
