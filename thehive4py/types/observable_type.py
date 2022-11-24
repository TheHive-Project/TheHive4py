from typing import TypedDict


class InputObservableTypeRequired(TypedDict):
    name: str


class InputObservableType(InputObservableTypeRequired, total=False):
    isAttachement: bool


class OutputObservableTypeRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    name: str
    isAttachement: bool


class OutputObservableType(OutputObservableTypeRequired, total=False):
    _updatedBy: str
    _updatedAt: int
