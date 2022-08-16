from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.custom_field import (
    InputCustomField,
    InputUpdateCustomField,
    OutputCustomField,
)


class CustomFieldEndpoint(EndpointBase):
    def create(self, custom_field: InputCustomField) -> OutputCustomField:
        return self._session.make_request(
            "POST", path="/api/v1/customField", json=custom_field
        )

    def list(self) -> List[OutputCustomField]:
        return self._session.make_request("GET", path="/api/v1/customField")

    def delete(self, custom_field_id: str) -> None:
        return self._session.make_request(
            "DELETE", path=f"/api/v1/customField/{custom_field_id}"
        )

    def update(self, custom_field_id: str, fields: InputUpdateCustomField) -> None:
        return self._session.make_request(
            "PATCH", path=f"/api/v1/customField/{custom_field_id}", json=fields
        )
