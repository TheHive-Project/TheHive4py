from .model import Model


class Case(Model):

    def __init__(self, data):
        defaults = {
            'id': None,
            'title': None,
            'description': None,
            'severity': 2,
            'owner': None,
            'startDate': None,
            'endDate': None,
            'flag': None,
            'tlp': 2,
            'tags': [],
            'caseId': None,
            'status': None,
            'resolutionStatus': None,
            'impactStatus': None,
            'summary': None,
            'mergedInto': None,
            'mergedFrom': None,
            'customFields': {},
            'metrics': {}
        }

        # TODO handle tasks
        # TODO handle observables

        if data is None:
            data = dict(defaults)

        self.__dict__ = {k: v for k, v in data.items() if not k.startswith('_')}