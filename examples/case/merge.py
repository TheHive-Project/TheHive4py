from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

case_ids_to_merge: list[str] = []
for i in range(2):
    case_to_merge = hive.case.create(
        case={
            "title": f"original case #{i}",
            "description": "a case to merge with another",
        }
    )
    case_ids_to_merge.append(case_to_merge["_id"])


merge_case = hive.case.merge(case_ids=case_ids_to_merge)
