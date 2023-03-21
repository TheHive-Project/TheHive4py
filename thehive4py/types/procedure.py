from typing import TypedDict


class InputProcedureRequired(TypedDict):
    occurDate: int
    patternId: str


class InputProcedure(InputProcedureRequired, total=False):
    tactic: str
    description: str


class OutputProcedureRequired(TypedDict):
    _id: str
    _createdAt: int
    _createdBy: str
    occurDate: int
    tactic: str
    tacticLabel: str
    extraData: dict


class OutputProcedure(OutputProcedureRequired, total=False):
    _updatedAt: int
    _updatedBy: str
    description: str
    patternId: str
    patternName: str


class InputUpdateProcedure(TypedDict, total=False):
    description: str
    occurDate: int
