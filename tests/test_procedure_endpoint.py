import pytest

from thehive4py.client import TheHiveApi
from thehive4py.errors import TheHiveError
from thehive4py.helpers import now_to_ts
from thehive4py.query.filters import In
from thehive4py.types.alert import OutputAlert
from thehive4py.types.case import OutputCase
from thehive4py.types.procedure import (
    InputProcedure,
    InputUpdateProcedure,
    OutputProcedure,
)


class TestProcedureEndpoint:
    def test_create_in_alert_and_get(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):
        created_procedure = thehive.procedure.create_in_alert(
            alert_id=test_alert["_id"],
            procedure={
                "occurDate": now_to_ts(),
                "patternId": "T1059.006",
                "tactic": "execution",
                "description": "...",
            },
        )

        fetched_procedure = thehive.procedure.get(procedure_id=created_procedure["_id"])
        assert created_procedure == fetched_procedure

    def test_bulk_create_in_alert_and_find(
        self, thehive: TheHiveApi, test_alert: OutputAlert
    ):
        procedures: list[InputProcedure] = [
            {
                "occurDate": now_to_ts(),
                "patternId": "T1059.006",
                "tactic": "execution",
                "description": "...",
            },
            {
                "occurDate": now_to_ts(),
                "patternId": "T1059.007",
                "tactic": "execution",
                "description": "...",
            },
        ]
        created_procedures = thehive.procedure.bulk_create_in_alert(
            alert_id=test_alert["_id"], procedures=procedures
        )

        fetched_procedures = thehive.procedure.find(
            filters=In(
                field="_id",
                values=[procedure["_id"] for procedure in created_procedures],
            )
        )
        assert sorted(
            created_procedures,
            key=lambda procedure: procedure["_id"],
        ) == sorted(
            fetched_procedures,
            key=lambda procedure: procedure["_id"],
        )

    def test_create_in_case_and_get(self, thehive: TheHiveApi, test_case: OutputCase):
        created_procedure = thehive.procedure.create_in_case(
            case_id=test_case["_id"],
            procedure={
                "occurDate": now_to_ts(),
                "patternId": "T1059.006",
                "tactic": "execution",
                "description": "...",
            },
        )

        fetched_procedure = thehive.procedure.get(procedure_id=created_procedure["_id"])
        assert created_procedure == fetched_procedure

    def test_bulk_create_in_case_and_find(
        self, thehive: TheHiveApi, test_case: OutputCase
    ):
        procedures: list[InputProcedure] = [
            {
                "occurDate": now_to_ts(),
                "patternId": "T1059.006",
                "tactic": "execution",
                "description": "...",
            },
            {
                "occurDate": now_to_ts(),
                "patternId": "T1059.007",
                "tactic": "execution",
                "description": "...",
            },
        ]
        created_procedures = thehive.procedure.bulk_create_in_case(
            case_id=test_case["_id"], procedures=procedures
        )
        fetched_procedures = thehive.procedure.find(
            filters=In(
                field="_id",
                values=[procedure["_id"] for procedure in created_procedures],
            )
        )
        assert sorted(
            created_procedures,
            key=lambda procedure: procedure["_id"],
        ) == sorted(
            fetched_procedures,
            key=lambda procedure: procedure["_id"],
        )

    def test_delete(self, thehive: TheHiveApi, test_procedure: OutputProcedure):
        procedure_id = test_procedure["_id"]
        thehive.procedure.delete(procedure_id=procedure_id)
        with pytest.raises(TheHiveError):
            thehive.procedure.get(procedure_id=procedure_id)

    def test_update(self, thehive: TheHiveApi, test_procedure: OutputProcedure):
        procedure_id = test_procedure["_id"]
        update_fields: InputUpdateProcedure = {
            "description": "updated procedure",
            "occurDate": now_to_ts(),
        }
        thehive.procedure.update(
            procedure_id=test_procedure["_id"], fields=update_fields
        )
        updated_procedure = thehive.procedure.get(procedure_id=procedure_id)

        for key, value in update_fields.items():
            assert updated_procedure.get(key) == value

    def test_bulk_delete(self, thehive: TheHiveApi, test_procedure: OutputProcedure):
        procedure_id = test_procedure["_id"]
        thehive.procedure.bulk_delete(procedure_ids=[procedure_id])
        with pytest.raises(TheHiveError):
            thehive.procedure.get(procedure_id=procedure_id)
