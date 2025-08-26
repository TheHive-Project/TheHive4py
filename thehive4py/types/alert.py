from typing import List, TypedDict

from typing_extensions import NotRequired

from thehive4py.types.custom_field import InputCustomFieldValue, OutputCustomFieldValue
from thehive4py.types.observable import InputObservable
from thehive4py.types.page import InputCasePage
from thehive4py.types.procedure import InputProcedure
from thehive4py.types.share import InputShare
from thehive4py.types.task import InputTask


class InputAlert(TypedDict):
    type: str
    source: str
    sourceRef: str
    externalLink: NotRequired[str]
    title: str
    description: str
    severity: NotRequired[int]
    date: NotRequired[int]
    tags: NotRequired[List[str]]
    flag: NotRequired[bool]
    tlp: NotRequired[int]
    pap: NotRequired[int]
    customFields: NotRequired[List[InputCustomFieldValue]]
    summary: NotRequired[str]
    status: NotRequired[str]
    assignee: NotRequired[str]
    caseTemplate: NotRequired[str]
    observables: NotRequired[List[InputObservable]]
    procedures: NotRequired[List[InputProcedure]]


class OutputAlert(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _updatedBy: NotRequired[str]
    _createdAt: int
    _updatedAt: NotRequired[int]
    type: str
    source: str
    sourceRef: str
    externalLink: NotRequired[str]
    title: str
    description: str
    severity: int
    severityLabel: str
    date: int
    tags: NotRequired[List[str]]
    tlp: int
    tlpLabel: str
    pap: int
    papLabel: str
    follow: bool
    customFields: NotRequired[List[OutputCustomFieldValue]]
    caseTemplate: NotRequired[str]
    observableCount: int
    caseId: NotRequired[str]
    status: str
    stage: str
    assignee: NotRequired[str]
    summary: NotRequired[str]
    extraData: dict
    newDate: int
    inProgressDate: NotRequired[int]
    closedDate: NotRequired[int]
    importedDate: NotRequired[int]
    timeToDetect: int
    timeToTriage: NotRequired[int]
    timeToQualify: NotRequired[int]
    timeToAcknowledge: NotRequired[int]


class InputUpdateAlert(TypedDict, total=False):
    type: str
    source: str
    sourceRef: str
    externalLink: str
    title: str
    description: str
    severity: int
    date: int
    lastSyncDate: int
    tags: List[str]
    tlp: int
    pap: int
    follow: bool
    customFields: List[InputCustomFieldValue]
    status: str
    summary: str
    assignee: str
    addTags: List[str]
    removeTags: List[str]


class InputBulkUpdateAlert(InputUpdateAlert):
    ids: List[str]


class InputPromoteAlert(TypedDict, total=False):
    title: str
    description: str
    severity: int
    startDate: int
    endDate: int
    tags: List[str]
    flag: bool
    tlp: int
    pap: int
    status: str
    summary: str
    assignee: str
    customFields: List[InputCustomFieldValue]
    caseTemplate: str
    tasks: List[InputTask]
    pages: List[InputCasePage]
    sharingParameters: List[InputShare]
    taskRule: str
    observableRule: str
