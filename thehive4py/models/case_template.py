from .model import Model
from .constants import Tlp, Pap, Severity


class CaseTemplate(Model):

    def __init__(self, data):
        defaults = {
            'titlePrefix': None,
            'name': None,
            'description': None,
            'tlp': Tlp.AMBER.value,
            'pap': Pap.AMBER.value,
            'severity': Severity.MEDIUM.value,
            'tags': [],
            'tasks': [],
            'customFields': {},
            'metrics': {}
        }

        if data is None:
            data = dict(defaults)

        properties = {}
        properties.update(defaults)
        properties.update(data)

        self.__dict__ = {k: v for k, v in properties.items() if not k.startswith('_')}
