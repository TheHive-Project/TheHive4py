from typing import List, TypedDict

from thehive4py.types.custom_field import InputCustomFieldValue, OutputCustomFieldValue
from thehive4py.types.observable import InputObservable


class InputAlertRequired(TypedDict):
    type: str
    source: str
    sourceRef: str
    title: str
    description: str
    date: int


class InputAlert(InputAlertRequired, total=False):
    externalLink: str
    severity: int
    tags: List[str]
    flag: bool
    tlp: int
    pap: int
    customFields: List[InputCustomFieldValue]
    summary: str
    status: str
    caseTemplate: str
    observables: List[InputObservable]


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
    date: int
    tlp: int
    pap: int
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


class InputBulkUpdateAlert(InputUpdateAlert):
    ids: List[str]
