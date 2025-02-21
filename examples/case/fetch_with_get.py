from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

case_to_get = hive.case.create(
    case={
        "title": "case to get",
        "description": "a single case to fetch",
    }
)


fetched_case = hive.case.get(case_id=case_to_get["_id"])
