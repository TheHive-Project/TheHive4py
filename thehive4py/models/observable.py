from .model import Model


class Observable(Model):

    def __init__(self, data):
        defaults = {
            'tlp': 2,
            'tags': [],
            'message': None,
            'ioc': False,
            'sighted': False
        }

        if data is None:
            data = dict(defaults)

        self.__dict__ = {k: v for k, v in {**defaults, **data}.items() if not k.startswith('_')}
