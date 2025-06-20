from typing import List, Literal, TypedDict, Union

from typing_extensions import Required

from .custom_field import InputCustomFieldValue
from .task import InputTask, OutputTask

SeverityValue = Literal[1, 2, 3, 4]
TlpValue = Literal[0, 1, 2, 3, 4]
PapValue = Literal[0, 1, 2, 3]


class InputCaseTemplate(TypedDict, total=False):
    name: Required[str]
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


class OutputCaseTemplate(TypedDict, total=False):
    _id: Required[str]
    _type: Required[str]
    _createdBy: Required[str]
    _updatedBy: str
    _createdAt: Required[int]
    _updatedAt: int
    name: Required[str]
    displayName: Required[str]
    titlePrefix: str
    description: str
    severity: SeverityValue
    severityLabel: str
    tags: List[str]
    flag: Required[bool]
    tlp: TlpValue
    tlpLabel: str
    pap: PapValue
    papLabel: str
    summary: str
    customFields: Union[dict, List[InputCustomFieldValue]]
    tasks: List[OutputTask]
    extraData: Required[dict]
