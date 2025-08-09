from typing import TypedDict

from typing_extensions import NotRequired


class InputComment(TypedDict):
    message: str


class OutputComment(TypedDict):
    _id: str
    _type: str
    createdBy: str
    createdAt: int
    updatedAt: NotRequired[int]
    updatedBy: NotRequired[str]
    message: str
    isEdited: bool
    extraData: dict


class InputUpdateComment(TypedDict):
    message: str
