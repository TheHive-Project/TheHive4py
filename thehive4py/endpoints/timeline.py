from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.timeline import (
    InputCustomEvent,
    InputUpdateCustomEvent,
    OutputCustomEvent,
    OutputTimeline,
)


class TimelineEndpoint(EndpointBase):
    def get(self, case_id: str) -> OutputTimeline:
        """
        Retrieves the timeline for a given case.

        Parameters:
            - case_id (str): The ID of the case.

        Returns:
            - OutputTimeline: The retrieved procedure.
        """
        return self._session.make_request("GET", f"/api/v1/case/{case_id}/timeline")

    def create_event(self, case_id: str, event: InputCustomEvent) -> OutputCustomEvent:
        """
        Create an event for a given case.

        Parameters:
            - case_id (str): The ID or name of the case to create the event for.
            - event (InputCustomEvent): The event to create.

        Returns:
            - OutputCustomEvent: The created event.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/customEvent", json=event
        )

    def delete_event(self, event_id: str) -> None:
        """
        Deletes a specified event.

        Parameters:
            - event_id (str): The ID of the event.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/customEvent/{event_id}"
        )

    def update_event(self, event_id: str, fields: InputUpdateCustomEvent) -> None:
        """
        Updates an existing event.

        Parameters:
            - event_id (str): The ID of the event to update.
            - fields (InputUpdateCustomEvent): The fields to update.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/customEvent/{event_id}", json=fields
        )
