from .model import Model


class Metric(Model):

    def __init__(self, data):
        defaults = {
            'title': None,
            'name': None,
            'description': None,
        }

        if data is None:
            data = dict(defaults)

        self.__dict__ = {k: v for k, v in {**defaults, **data}.items() if not k.startswith('_')}
