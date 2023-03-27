from typing import Dict


class OutputPatternRequired(Dict):
    _id: str
    _type: str
    _createdAt: int
    _createdBy: str
    name: int
    dataSource: list
    detection: str
    patternId: str
    patternType: str
    platforms: list
    remoteSupport: bool
    revoked: bool
    tactics: list
    url: str
    version: str


class OutputPattern(OutputPatternRequired):
    description: str
    defenseBypassed: list
    permissionsRequired: list
    systemRequirements: list
