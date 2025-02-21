from thehive4py import TheHiveApi
from thehive4py.query.filters import Eq

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

antivirus_case = hive.case.create(
    case={
        "title": "case #1 to find",
        "description": "a case to find with others",
        "tags": ["antivirus"],
    }
)

phishing_case = hive.case.create(
    case={
        "title": "case #2 to find",
        "description": "a case to find with others",
        "tags": ["phishing"],
    }
)


filters = Eq(field="tags", value="antivirus") | Eq(field="tags", value="phishing")
fetched_cases = hive.case.find(filters=filters)
