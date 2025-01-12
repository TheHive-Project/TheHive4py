from typing import List, TypedDict

from thehive4py.types.custom_field import InputCustomFieldValue, OutputCustomFieldValue
from thehive4py.types.observable import InputObservable
from thehive4py.types.page import InputCasePage
from thehive4py.types.procedure import InputProcedure
from thehive4py.types.share import InputShare
from thehive4py.types.task import InputTask


class InputAlertRequired(TypedDict):
    type: str
    source: str
    sourceRef: str
    title: str
    description: str


class InputAlert(InputAlertRequired, total=False):
    date: int
    externalLink: str
    severity: int
    tags: List[str]
    flag: bool
    tlp: int
    pap: int
    customFields: List[InputCustomFieldValue]
    summary: str
    status: str
    assignee: str
    caseTemplate: str
    observables: List[InputObservable]
    procedures: List[InputProcedure]


class OutputAlertRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    type: str
    source: str
    sourceRef: str
    title: str
    description: str
    severity: int
    severityLabel: str
    date: int
    tlp: int
    tlpLabel: str
    pap: int
    papLabel: str
    follow: bool
    observableCount: int
    status: str
    stage: str
    extraData: dict
    newDate: int
    timeToDetect: int


class OutputAlert(OutputAlertRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    externalLink: str
    tags: List[str]
    customFields: List[OutputCustomFieldValue]
    caseTemplate: str
    caseId: str
    assignee: str
    summary: str
    inProgressDate: int
    closedDate: int
    importedDate: int
    timeToTriage: int
    timeToQualify: int
    timeToAcknowledge: int


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
