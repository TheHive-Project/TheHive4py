from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

minimalistic_case = hive.case.create(
    case={
        "title": "a minimalistic case",
        "description": "a bit too minimal",
    }
)
