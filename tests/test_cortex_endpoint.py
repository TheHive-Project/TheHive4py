from typing import List

from thehive4py.client import TheHiveApi
from thehive4py.query.filters import Id
from thehive4py.types.case import OutputCase
from thehive4py.types.observable import OutputObservable


class TestCortexEndpoint:
    def test_create_and_get_analyzer_job(
        self, thehive: TheHiveApi, test_observable: OutputObservable
    ):
        created_analyzer_job = thehive.cortex.create_analyzer_job(
            job={
                "analyzerId": "example",
                "cortexId": "cortex",
                "artifactId": test_observable["_id"],
            }
        )
        assert created_analyzer_job["_type"] == "case_artifact_job"
        fetched_analyzer_job = thehive.cortex.get_analyzer_job(
            job_id=created_analyzer_job["_id"]
        )
        assert created_analyzer_job["_id"] == fetched_analyzer_job["_id"]

    def test_create_and_find_analyzer_job(
        self, thehive: TheHiveApi, test_observable: OutputObservable
    ):
        created_analyzer_job = thehive.cortex.create_analyzer_job(
            job={
                "analyzerId": "dummy-analyzer",
                "cortexId": "dummy-cortex",
                "artifactId": test_observable["_id"],
            }
        )

        found_analyzer_jobs = thehive.cortex.find_analyzer_jobs(
            filters=Id(id=created_analyzer_job["_id"])
        )

        assert len(found_analyzer_jobs) == 1
        assert found_analyzer_jobs[0]["_id"] == created_analyzer_job["_id"]

    def test_create_analyzer_jobs_in_bulk(
        self, thehive: TheHiveApi, test_observables: List[OutputObservable]
    ):
        created_analyzer_jobs = thehive.cortex.bulk_create_analyzer_jobs(
            jobs=[
                {
                    "analyzerId": "dummy-analyzer",
                    "cortexId": "dummy-cortex",
                    "artifactId": observable["_id"],
                }
                for observable in test_observables
            ]
        )

        assert len(created_analyzer_jobs) == 2
        for job in created_analyzer_jobs:
            assert job["_type"] == "case_artifact_job"

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
