from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

original_case = hive.case.create(
    case={
        "title": "original case",
        "description": "a single case to update",
    }
)


hive.case.update(
    case_id=original_case["_id"],
    fields={
        "title": "updated case",
        "tags": ["update-single"],
    },
)

updated_case = hive.case.get(case_id=original_case["_id"])
