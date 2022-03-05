from typing import List, TypedDict


class OutputTimelineEventRequired(TypedDict):
    date: int
    kind: str
    entity: str
    entityId: str
    details: dict


class OutputTimelineEvent(OutputTimelineEventRequired, total=False):
    endDate: int


class OutputTimeline(TypedDict):
    events: List[OutputTimelineEvent]


class InputCustomEventRequired(TypedDict):
    date: int
    title: str


class InputCustomEvent(InputCustomEventRequired, total=False):
    endDate: int
    description: str


class OutputCustomEventRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    date: int
    title: str


class OutputCustomEvent(OutputCustomEventRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    endDate: int
    description: str


class InputUpdateCustomEvent(TypedDict, total=False):
    date: int
    endDate: int
    title: str
    description: str
