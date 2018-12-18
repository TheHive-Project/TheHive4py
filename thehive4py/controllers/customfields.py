from typing import List

from .dblist import DBListController
from ..models import CustomField


class CustomFieldsController(DBListController):
    def __init__(self, api):
        DBListController.__init__(self, 'custom_fields', api)

    def find_all(self) -> List[CustomField]:
        return self._wrap(self._find_all(), CustomField)

    def get_by_id(self, item_id) -> CustomField:
        return self._wrap(self._get_by_id(item_id), CustomField)

    def create(self, data) -> CustomField:
        if isinstance(data, dict):
            data = CustomField(data).json()
        elif isinstance(data, CustomField):
            data = data.json()

        return CustomField(self._create(data))
