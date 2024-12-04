from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.cortex import (
    OutputAnalyzer,
    OutputAnalyzerJob,
    OutputResponder,
    OutputResponderAction,
    InputResponderAction,
    InputAnalyzerJob,
)
from typing import Optional, List


class CortexEndpoint(EndpointBase):
    def create_analyzer_job(self, job: InputAnalyzerJob) -> OutputAnalyzerJob:
        return self._session.make_request(
            "POST", path="/api/connector/cortex/job", json=job
        )

    def create_responder_action(
        self, action: InputResponderAction
    ) -> OutputResponderAction:
        return self._session.make_request(
            "POST", path="/api/connector/cortex/action", json=action
        )

    def list_analyzers(self, range: Optional[str] = None) -> List[OutputAnalyzer]:
        params = {"range": range}
        return self._session.make_request(
            "GET", path="/api/connector/cortex/analyzer", params=params
        )

    def list_analyzers_by_type(self, data_type: str) -> List[OutputAnalyzer]:
        return self._session.make_request(
            "GET", path=f"/api/connector/cortex/analyzer/type/{data_type}"
        )

    def get_analyzer(self, analyzer_id: str) -> OutputAnalyzer:
        return self._session.make_request(
            "GET", path=f"/api/connector/cortex/analyzer/{analyzer_id}"
        )

    def get_analyzer_job(self, job_id: str) -> OutputAnalyzerJob:
        return self._session.make_request(
            "GET", path=f"/api/connector/cortex/job/{job_id}"
        )

    def list_responders(
        self, entity_type: str, entity_id: str
    ) -> List[OutputResponder]:
        return self._session.make_request(
            "GET", f"/api/connector/cortex/responder/{entity_type}/{entity_id}"
        )
