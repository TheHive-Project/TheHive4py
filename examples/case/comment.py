from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

case = hive.case.create(
    case={
        "title": "case with a comment",
        "description": "a case to comment on",
    },
)

hive.comment.create_in_case(
    case_id=case["_id"],
    comment={"message": "what an average case to comment on"},
)
