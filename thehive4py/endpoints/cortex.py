from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.cortex import (
    OutputAnalyzer,
    OutputAnalyzerJob,
    OutputResponder,
    OutputResponderAction,
)
from typing import Optional


class CortexEndpoint(EndpointBase):
    def create_analyzer_job(
        self, cortex_id: str, analyzer_id: str, observable_id: str
    ) -> OutputAnalyzerJob:
        return self._session.make_request(
            "POST",
            path="/api/connector/cortex/job",
            json={
                "analyzerId": analyzer_id,
                "cortexId": cortex_id,
                "artifactId": observable_id,
            },
        )

    def create_responder_action(
        self, object_id: str, object_type: str, responder_id: str
    ) -> OutputResponderAction:
        return self._session.make_request(
            "POST",
            path="/api/connector/cortex/action",
            json={
                "objectId": object_id,
                "objectType": object_type,
                "responderId": responder_id,
            },
        )

    def list_analyzers(self, range: Optional[str] = None) -> list[OutputAnalyzer]:
        payload = {"range": range} if range else None
        return self._session.make_request(
            "GET", path="/api/connector/cortex/analyzer", json=payload
        )

    def list_analyzers_by_type(self, data_type: str) -> list[OutputAnalyzer]:
        return self._session.make_request(
            "GET", path=f"/api/connector/cortex/analyzer/type/{data_type}"
        )

    def get_analyzer(self, object_id: str) -> OutputAnalyzer:
        return self._session.make_request(
            "GET", path=f"/api/connector/cortex/analyzer/{object_id}"
        )

    def get_analyzer_job(self, job_id: str) -> OutputAnalyzerJob:
        return self._session.make_request(
            "GET", path=f"/api/connector/cortex/job/{job_id}"
        )

    def list_responders(
        self, entity_type: str, entity_id: str
    ) -> list[OutputResponder]:
        return self._session.make_request(
            "GET", f"/api/connector/cortex/responder/{entity_type}/{entity_id}"
        )
