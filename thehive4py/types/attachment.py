from typing import List, TypedDict


class OutputAttachmentRequired(TypedDict):
    _id: str
    _type: str
    _createdBy: str
    _createdAt: int
    name: str
    size: int
    contentType: str
    id: str


class OutputAttachment(OutputAttachmentRequired, total=False):
    _updatedBy: str
    _updatedAt: int
    hashes: List[str]
