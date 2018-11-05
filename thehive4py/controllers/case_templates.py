import os
import magic
import json

from typing import List

from .abstract import AbstractController
from ..models import CaseTemplate
from ..query import *


class CaseTemplateController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'case/template', api)

    def find_all(self, query, **kwargs) -> List[CaseTemplate]:
        return self._wrap(self._find_all(query, **kwargs), CaseTemplate)

    def find_one_by(self, query, **kwargs) -> CaseTemplate:
        return self._wrap(self._find_one_by(query, **kwargs), CaseTemplate)

    def get_by_id(self, org_id) -> CaseTemplate:
        return self._wrap(self._get_by_id(org_id), CaseTemplate)

    def create(self, data) -> CaseTemplate:
        if isinstance(data, dict):
            data = CaseTemplate(data).json()
        elif isinstance(data, CaseTemplate):
            data = data.json()

        return CaseTemplate(self._api.do_post('case/template', data).json())

    def update(self, template_id, data, fields=None) -> CaseTemplate:
        url = 'case/template/{}'.format(template_id)

        updatable_fields = [
            'name',
            'titlePrefix',
            'description',
            'severity',
            'tlp',
            'pap',
            'tags',
            'tasks',
            'metrics',
            'customFields'
        ]
        patch = AbstractController._clean_changes(data, updatable_fields, fields)
        return self._wrap(self._api.do_patch(url, patch).json(), CaseTemplate)

    def remove(self, template_id) -> bool:
        return self._api.do_delete('case/template/{}'.format(template_id))