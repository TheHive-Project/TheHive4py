from .model import Model


class Case(Model):

    def __init__(self, data):
        defaults = {
            'title': None,
            'description': None,
            'tlp': 2,
            'severity': 2,
            'startDate': None,
            'flag': False,
            'tags': [],
            'customFields': {},
            'metrics': {}
        }

        if data is None:
            data = dict(defaults)

        self.__dict__ = {k: v for k, v in {**defaults, **data}.items() if not k.startswith('_')}