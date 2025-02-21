from thehive4py import TheHiveApi
from thehive4py.helpers import now_to_ts
from thehive4py.types.procedure import InputProcedure

hive = TheHiveApi(url="thehive.example", apikey="h1v3b33")

case_to_enrich = hive.case.create(
    case={
        "title": "case to enrich",
        "description": "a case to enrich with procedures",
    }
)

case_procedures: list[InputProcedure] = [
    {
        "occurDate": now_to_ts(),
        "patternId": "T1566",
        "tactic": "initial-access",
        "description": "Phishing",
    },
    {
        "occurDate": now_to_ts(),
        "patternId": "T1566.001",
        "tactic": "initial-access",
        "description": "Spearphishing Attachment",
    },
]


for procedure in case_procedures:
    hive.case.create_procedure(case_id=case_to_enrich["_id"], procedure=procedure)
