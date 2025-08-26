from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.timeline import (
    InputCustomEvent,
    InputUpdateCustomEvent,
    OutputCustomEvent,
    OutputTimeline,
)


class TimelineEndpoint(EndpointBase):
    def get(self, case_id: str) -> OutputTimeline:
        """Retrieve the timeline of a case.

        Args:
            case_id: The id of the case whose timeline is to be retrieved.

        Returns:
            The timeline of the specified case.
        """
        return self._session.make_request("GET", f"/api/v1/case/{case_id}/timeline")

    def create_event(self, case_id: str, event: InputCustomEvent) -> OutputCustomEvent:
        """Create a custom event in a case's timeline.

        Args:
            case_id: The id of the case to add the custom event to.
            event: The body of custom event.

        Returns:
            The created custom event.
        """
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/customEvent", json=event
        )

    def delete_event(self, event_id: str) -> None:
        """Delete a custom event by id.

        Args:
            event_id: The id of the custom event to delete.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/customEvent/{event_id}"
        )

    def update_event(self, event_id: str, fields: InputUpdateCustomEvent) -> None:
        """Update a custom event.

        Args:
            event_id: The id of the custom event to update.
            fields: The fields to update in the custom event.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/customEvent/{event_id}", json=fields
        )
