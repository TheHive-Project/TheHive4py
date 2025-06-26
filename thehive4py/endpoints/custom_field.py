from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.custom_field import (
    InputCustomField,
    InputUpdateCustomField,
    OutputCustomField,
)


class CustomFieldEndpoint(EndpointBase):
    def list(self) -> List[OutputCustomField]:
        """List all custom fields.

        Returns:
            The list of all custom fields.
        """
        return self._session.make_request("GET", path="/api/v1/customField")

    def create(self, custom_field: InputCustomField) -> OutputCustomField:
        """Create a custom field.

        Args:
            custom_field: The body of the custom field.

        Returns:
            The created custom field.
        """
        return self._session.make_request(
            "POST", path="/api/v1/customField", json=custom_field
        )

    def delete(self, custom_field_id: str, force: bool = False) -> None:
        """Delete a custom field.

        Args:
            custom_field_id: The id of the custom field.
            force: Whether to forcefully delete the custom field.

        Returns:
            N/A
        """
        return self._session.make_request(
            "DELETE",
            path=f"/api/v1/customField/{custom_field_id}",
            params={"force": force},
        )

    def update(self, custom_field_id: str, fields: InputUpdateCustomField) -> None:
        """Update a custom field.

        Args:
            custom_field_id: The id of the custom field.
            fields: The fields of the custom field to update.

        Returns:
            N/A
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/customField/{custom_field_id}", json=fields
        )
