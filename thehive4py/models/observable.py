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

        properties = {}
        properties.update(defaults)
        properties.update(data)

        self.__dict__ = {k: v for k, v in properties.items() if not k.startswith('_')}
