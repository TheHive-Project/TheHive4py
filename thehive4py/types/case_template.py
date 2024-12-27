from typing import List, Literal, TypedDict, Union

from .custom_field import InputCustomFieldValue
from .task import InputTask, OutputTask

SeverityValue = Literal[1, 2, 3, 4]
TlpValue = Literal[0, 1, 2, 3, 4]
PapValue = Literal[0, 1, 2, 3]


class InputCaseTemplateRequired(TypedDict):
    name: str


class InputCaseTemplate(InputCaseTemplateRequired, total=False):
    displayName: str
    titlePrefix: str
    description: str
    severity: SeverityValue
    tags: List[str]
    flag: bool
    tlp: TlpValue
    pap: PapValue
    summary: str
    tasks: List[InputTask]
    pageTemplateIds: List[str]
    customFields: Union[dict, List[InputCustomFieldValue]]


class OutputCaseTemplateRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    name: str


class OutputCaseTemplate(OutputCaseTemplateRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    displayName: str
    titlePrefix: str
    description: str
    severity: SeverityValue
    tags: List[str]
    flag: bool
    tlp: TlpValue
    pap: PapValue
    summary: str
    tasks: List[OutputTask]
    pageTemplateIds: List[str]
    customFields: Union[dict, List[InputCustomFieldValue]]
