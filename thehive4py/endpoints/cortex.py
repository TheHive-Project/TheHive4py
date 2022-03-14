from thehive4py.endpoints._base import EndpointBase


class CortexEndpoint(EndpointBase):
    def create_analyzer_job(
        self, cortex_id: str, analyzer_id: str, observable_id: str
    ) -> dict:
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
    ) -> dict:
        return self._session.make_request(
            "POST",
            path="/api/connector/cortex/action",
            json={
                "objectId": object_id,
                "objectType": object_type,
                "responderId": responder_id,
            },
        )
