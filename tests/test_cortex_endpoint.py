from thehive4py.client import TheHiveApi
from thehive4py.types.case import OutputCase
from thehive4py.types.observable import OutputObservable


class TestCortexEndpoint:
    def test_create_analyzer_job(
        self, thehive: TheHiveApi, test_observable: OutputObservable
    ):
        output_analyzer_job = thehive.cortex.create_analyzer_job(
            job={
                "analyzerId": "example",
                "cortexId": "cortex",
                "artifactId": test_observable["_id"],
            }
        )
        assert output_analyzer_job["_type"] == "case_artifact_job"

    def test_list_analyzers(self, thehive: TheHiveApi):
        analyzers = thehive.cortex.list_analyzers()
        assert analyzers == []

    def test_list_analyzers_by_type(self, thehive: TheHiveApi):
        data_type = "mail"
        analyzers = thehive.cortex.list_analyzers_by_type(data_type=data_type)
        assert analyzers == []

    def test_list_responders(self, thehive: TheHiveApi, test_case: OutputCase):
        responders = thehive.cortex.list_responders(
            entity_type="case", entity_id=test_case["_id"]
        )
        assert responders == []
