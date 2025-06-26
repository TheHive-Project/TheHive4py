from typing import TypedDict

from typing_extensions import NotRequired


class InputProcedure(TypedDict):
    occurDate: int
    patternId: str
    tactic: NotRequired[str]
    description: NotRequired[str]


class OutputProcedure(TypedDict):
    _id: str
    _createdAt: int
    _createdBy: str
    _updatedAt: NotRequired[int]
    _updatedBy: NotRequired[str]
    description: NotRequired[str]
    occurDate: int
    patternId: NotRequired[str]
    patternName: NotRequired[str]
    tactic: NotRequired[str]
    tacticLabel: NotRequired[str]
    extraData: dict


class InputUpdateProcedure(TypedDict, total=False):
    description: str
    occurDate: int
    patternId: str
    tactic: str
