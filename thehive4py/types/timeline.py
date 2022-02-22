from typing import TypedDict


class OutputTimelineEventRequired(TypedDict):
    date: int
    kind: str
    entity: str
    entityId: str
    details: dict


class OutputTimelineEvent(OutputTimelineEventRequired, total=False):
    endDate: int
