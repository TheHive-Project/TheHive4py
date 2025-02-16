from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

original_case_ids = []
for i in range(2):
    original_case = hive.case.create(
        case={
            "title": f"original case #{i}",
            "description": "a case to update in bulk",
        }
    )

    original_case_ids.append(original_case["_id"])


hive.case.bulk_update(
    fields={
        "ids": original_case_ids,
        "title": "bulk updated case",
        "tags": ["update-bulk"],
    },
)
