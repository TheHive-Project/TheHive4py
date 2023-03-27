from typing import Dict


class OutputCatalogRequired(Dict):
    _id: str
    _type: str
    createdAt: int
    createdBy: str
    name: int
    variant: str
    extraData: dict


class OutputCatalog(OutputCatalogRequired):
    description: str
