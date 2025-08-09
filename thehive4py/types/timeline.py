from typing import List, TypedDict

from typing_extensions import NotRequired


class OutputTimelineEvent(TypedDict):
    date: int
    kind: str
    entity: str
    entityId: str
    details: dict
    endDate: NotRequired[int]


class OutputTimeline(TypedDict):
    events: List[OutputTimelineEvent]


class InputCustomEvent(TypedDict):
    date: int
    endDate: NotRequired[int]
    title: str
    description: NotRequired[str]


class OutputCustomEvent(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    date: int
    endDate: NotRequired[int]
    title: str
    description: NotRequired[str]


class InputUpdateCustomEvent(TypedDict, total=False):
    date: int
    endDate: int
    title: str
    description: str
