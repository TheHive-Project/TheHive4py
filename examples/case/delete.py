from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

case_to_delete = hive.case.create(
    case={
        "title": "delete case",
        "description": "an case to delete",
    }
)


hive.case.delete(case_id=case_to_delete["_id"])
