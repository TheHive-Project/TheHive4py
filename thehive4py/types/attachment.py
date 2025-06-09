from typing import List, TypedDict


class InputAttachment(TypedDict):
    name: str
    contentType: str
    id: str


class OutputAttachmentRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    name: str
    hashes: List[str]
    size: int
    contentType: str
    id: str
    path: str
    extraData: dict


class OutputAttachment(OutputAttachmentRequired, total=False):
    _updatedBy: str
    _updatedAt: int
