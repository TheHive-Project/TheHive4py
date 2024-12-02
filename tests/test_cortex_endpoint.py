from thehive4py.client import TheHiveApi


class TestCortexEndpoint:
    def test_list_analyzers(self, thehive: TheHiveApi):
        analyzers = thehive.cortex.list_analyzers()
        assert isinstance(analyzers, list)
        for analyzer in analyzers:
            assert "name" in analyzer.keys()
            assert "id" in analyzer.keys()

    def test_list_analyzers_by_type(self, thehive: TheHiveApi):
        data_type = "mail"
        analyzers = thehive.cortex.list_analyzers_by_type(data_type=data_type)
        assert isinstance(analyzers, list)
        for analyzer in analyzers:
            assert "name" in analyzer.keys()
            assert "id" in analyzer.keys()

    def test_list_and_get_analyzers(self, thehive: TheHiveApi):
        analyzers = thehive.cortex.list_analyzers()
        for analyzer in analyzers:
            _analyzer = thehive.cortex.get_analyzer(analyzer["id"])
            assert _analyzer == analyzer

    def test_list_responders(self, thehive: TheHiveApi):
        thehive.case.create(case={"title": "my first case", "description": "..."})
        entity_type = "case"
        entity_id = thehive.case.find()[0]["_id"]
        responders = thehive.cortex.list_responders(
            entity_type=entity_type, entity_id=entity_id
        )
        assert isinstance(responders, list)
        for responder in responders:
            assert "name" in responder.keys()
            assert "id" in responder.keys()
