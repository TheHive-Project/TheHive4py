from thehive4py.client import TheHiveApi
from thehive4py.types.case import OutputCase

class TestCortexEndpoint:
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
        assert isinstance(responders, list)
