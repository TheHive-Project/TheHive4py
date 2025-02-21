from thehive4py import TheHiveApi
from thehive4py.types.case import InputCase

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

input_case: InputCase = {
    "title": "an advanced case",
    "description": "a bit more advanced case...",
    "caseTemplate": "my-template",
    "severity": 1,
    "status": "New",
    "tags": ["advanced", "example"],
}

output_case = hive.case.create(case=input_case)
