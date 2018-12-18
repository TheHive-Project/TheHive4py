from typing import List

from .abstract import AbstractController
from ..models import Alert, Case


class AlertsController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'alert', api)

    def find_all(self, query, **kwargs) -> List[Alert]:
        return self._wrap(self._find_all(query, **kwargs), Alert)

    def find_one_by(self, query, **kwargs) -> Alert:
        return self._wrap(self._find_one_by(query, **kwargs), Alert)

    def get_by_id(self, id) -> Alert:
        return self._wrap(self._get_by_id(id), Alert)

    def get_by_ref(self, ref) -> Alert:
        return self._wrap(self._find_one_by(Eq('sourceRef', ref)), Alert)

    def create(self, data) -> Alert:
        if isinstance(data, dict):
            data = Alert(data).json()
        elif isinstance(data, Alert):
            data = data.json()

        return Alert(self._api.do_post('alert', data).json())

    def update(self, alert_id, data, fields=None) -> Alert:
        url = 'alert/{}'.format(alert_id)
        updatable_fields = [
            'title',
            'type',
            'source',
            'sourceRef',
            'tlp',
            'severity',
            'tags',
            'description',
            'customFields',
            'artifacts'
        ]
        patch = AbstractController._clean_changes(data, updatable_fields, fields)
        return self._wrap(self._api.do_patch(url, patch).json(), Alert)

    def stats_by(self, query, field, top=10):
        return self._stats_by(query, field, top)

    def mark_as_read(self, alert_id) -> Alert:
        url = 'alert/{}/markAsRead'.format(alert_id)
        return self._wrap(self._api.do_post(url, {}).json(), Alert)

    def mark_as_unread(self, alert_id) -> Alert:
        url = 'alert/{}/markAsUnread'.format(alert_id)
        return self._wrap(self._api.do_post(url, {}).json(), Alert)

    def follow(self, alert_id) -> Alert:
        url = 'alert/{}/follow'.format(alert_id)
        return self._wrap(self._api.do_post(url, {}).json(), Alert)

    def unfollow(self, alert_id) -> Alert:
        url = 'alert/{}/unfollow'.format(alert_id)
        return self._wrap(self._api.do_post(url, {}).json(), Alert)

    def import_as_case(self, alert_id, template=None) -> Case:
        url = 'alert/{}/createCase'.format(alert_id)
        return self._wrap(self._api.do_post(url, {'caseTemplate': template}).json(), Case)

    def merge_into(self, alert_id, case_id) -> Case:
        url = 'alert/{}/merge/{}'.format(alert_id, case_id)
        return self._wrap(self._api.do_post(url, {}).json(), Case)
