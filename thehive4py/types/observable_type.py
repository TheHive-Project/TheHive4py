from typing import TypedDict


class InputObservableTypeRequired(TypedDict):
    name: str


class InputObservableType(InputObservableTypeRequired, total=False):
    isAttachment: bool


class OutputObservableTypeRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    name: str
    isAttachment: bool


class OutputObservableType(OutputObservableTypeRequired, total=False):
    _updatedBy: str
    _updatedAt: int
