from .model import Model


class Task(Model):

    def __init__(self, data):
        defaults = {
            'title': None,
            'description': None,
            'owner': None,
            'order': 0,
            'flag': False,
            'group': 'default',
            'startDate': None,
            'endDate': None
        }

        if data is None:
            data = dict(defaults)

        self.__dict__ = {k: v for k, v in {**defaults, **data}.items() if not k.startswith('_')}
