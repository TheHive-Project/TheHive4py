from typing import TypedDict


class InputComment(TypedDict):
    message: str


class OutputCommentRequired(TypedDict):
    _id: str
    _type: str
    createdBy: str
    createdAt: int
    message: str
    isEdited: bool


class OutputComment(OutputCommentRequired, total=False):
    updatedAt: str


class InputUpdateComment(TypedDict):
    message: str
