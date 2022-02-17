from typing import List, TypedDict

from thehive4py.types.custom_field import InputCustomFieldValue, OutputCustomFieldValue


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
    customFieldValue: List[InputCustomFieldValue]


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
    tags: List[str]
    tlp: int
    pap: int
    read: bool
    follow: bool
    customFields: List[OutputCustomFieldValue]
    observableCount: int
    extraData: dict


class OutputAlert(OutputAlertRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    externalLink: str
    caseTemplate: str
    caseId: str
