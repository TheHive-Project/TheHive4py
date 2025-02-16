from thehive4py import TheHiveApi
from thehive4py.types.page import InputCasePage

hive = TheHiveApi(url="thehive.example", apikey="h1v3b33")


case_to_enrich = hive.case.create(
    case={
        "title": "case to enrich",
        "description": "a case to enrich with pages",
    }
)

case_pages: list[InputCasePage] = [
    {
        "title": "Playbooks",
        "category": "general",
        "content": "Some playbook content",
    },
    {
        "title": "Resources",
        "category": "general",
        "content": "Some useful resources",
    },
]


for case_page in case_pages:
    hive.case.create_page(case_id=case_to_enrich["_id"], page=case_page)
