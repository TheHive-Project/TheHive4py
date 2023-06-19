from typing import List

from thehive4py.endpoints._base import EndpointBase
from thehive4py.types.custom_field import (
    InputCustomField,
    InputUpdateCustomField,
    OutputCustomField,
)


class CustomFieldEndpoint(EndpointBase):
    """
    Class representing TheHive's custom field endpoint.

    Parameters :
        - EndpointBase: TheHive4py EndpointBase class
    """

    def create(self, custom_field: InputCustomField) -> OutputCustomField:
        """
        Creates a new custom field.

        Parameters:
            - custom_field (InputCustomField): An object containing the custom field data.

        Returns:
            - OutputCustomField: An object containing the created custom field data.

        """
        return self._session.make_request(
            "POST", path="/api/v1/customField", json=custom_field
        )

    def list(self) -> List[OutputCustomField]:
        """
        Gets a list of all custom fields.

        Returns:
            - List[OutputCustomField]: A list of objects containing the custom field data.

        """
        return self._session.make_request("GET", path="/api/v1/customField")

    def delete(self, custom_field_id: str) -> None:
        """
        Deletes the specified custom field.

        Parameters:
            - custom_field_id (str): The ID of the custom field.

        Returns:
            None
        """
        return self._session.make_request(
            "DELETE", path=f"/api/v1/customField/{custom_field_id}"
        )

    def update(self, custom_field_id: str, fields: InputUpdateCustomField) -> None:
        """
        Updates the specified custom field with the provided fields.

        Parameters:
            - custom_field_id (str): The ID of the custom field.
            - fields (InputUpdateCustomField): An object containing the updated custom field data.

        Returns:
            None
        """
        return self._session.make_request(
            "PATCH", path=f"/api/v1/customField/{custom_field_id}", json=fields
        )
