from thehive4py.endpoints._base import EndpointBase


class CortexEndpoint(EndpointBase):
    def create_analyzer_job(
        self, cortex_id: str, analyzer_id: str, observable_id: str
    ) -> dict:
        """
        Creates an analyzer job for the given `analyzer_id`, `cortex_id`, and `observable_id`.

        Parameters:
            cortex_id (str): The ID of the Cortex instance to create the job on.
            analyzer_id (str): The ID of the analyzer to use for the job.
            observable_id (str): The ID of the observable to analyze.

        Returns:
            dict: A dictionary representing the newly created analyzer job.
        """
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
        """
        Creates a responder action for the given `object_id`, `object_type`, and `responder_id`.

        Parameters:
            object_id (str): The ID of the object to perform the action on.
            object_type (str): The type of the object to perform the action on.
            responder_id (str): The ID of the responder to use for the action.

        Returns:
            dict: A dictionary representing the newly created responder action.
        """
        return self._session.make_request(
            "POST",
            path="/api/connector/cortex/action",
            json={
                "objectId": object_id,
                "objectType": object_type,
                "responderId": responder_id,
            },
        )
