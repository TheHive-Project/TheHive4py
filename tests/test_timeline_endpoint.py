from thehive4py.client import TheHiveApi
from thehive4py.helpers import now_to_ts
from thehive4py.types.case import OutputCase
from thehive4py.types.timeline import InputUpdateCustomEvent, OutputCustomEvent


class TestTimelineEndpoint:
    def test_get(self, thehive: TheHiveApi, test_case: OutputCase):
        timeline = thehive.timeline.get(case_id=test_case["_id"])
        assert timeline["events"]

    def test_create_and_delete_event(self, thehive: TheHiveApi, test_case: OutputCase):
        timeline_event = thehive.timeline.create_event(
            case_id=test_case["_id"],
            event={"date": now_to_ts(), "title": "custom timeline event"},
        )

        timeline_events = thehive.timeline.get(case_id=test_case["_id"])["events"]
        assert timeline_event["_id"] in [event["entityId"] for event in timeline_events]

        thehive.timeline.delete_event(event_id=timeline_event["_id"])
        timeline_events = thehive.timeline.get(case_id=test_case["_id"])["events"]
        assert timeline_event["_id"] not in [
            event["entityId"] for event in timeline_events
        ]

    def test_update_event(
        self, thehive: TheHiveApi, test_timeline_event: OutputCustomEvent
    ):
        event_id = test_timeline_event["_id"]
        update_fields: InputUpdateCustomEvent = {
            "date": now_to_ts(),
            "endDate": now_to_ts(),
            "title": "updated event",
            "description": "updated event description",
        }
        thehive.timeline.update_event(event_id=event_id, fields=update_fields)
