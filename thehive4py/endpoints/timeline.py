from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.timeline import (
    InputCustomEvent,
    InputUpdateCustomEvent,
    OutputCustomEvent,
    OutputTimeline,
)


class TimelineEndpoint(EndpointBase):
    def get(self, case_id: str) -> OutputTimeline:
        return self._session.make_request("GET", f"/api/v1/case/{case_id}/timeline")

    def create_event(self, case_id: str, event: InputCustomEvent) -> OutputCustomEvent:
        return self._session.make_request(
            "POST", path=f"/api/v1/case/{case_id}/customEvent", json=event
        )

    def delete_event(self, event_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/customEvent/{event_id}"
        )

    def update_event(self, event_id: str, fields: InputUpdateCustomEvent) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/customEvent/{event_id}", json=fields
        )
