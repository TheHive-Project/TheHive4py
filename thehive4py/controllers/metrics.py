from typing import List

from .dblist import DBListController
from ..models import Metric


class MetricsController(DBListController):
    def __init__(self, api):
        DBListController.__init__(self, 'case_metrics', api)

    def find_all(self) -> List[Metric]:
        return self._wrap(self._find_all(), Metric)

    def get_by_id(self, item_id) -> Metric:
        return self._wrap(self._get_by_id(item_id), Metric)

    def create(self, data) -> Metric:
        if isinstance(data, dict):
            data = Metric(data).json()
        elif isinstance(data, Metric):
            data = data.json()

        return Metric(self._create(data))
