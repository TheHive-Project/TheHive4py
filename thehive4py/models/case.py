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

        # TODO handle tasks
        # TODO handle observables

        if data is None:
            data = dict(defaults)

        # tasks = []
        # if 'tasks' in data:
        #     for task in data['tasks']:
        #         if type(task) == Task:
        #             tasks.append(task.json())
        #         else:
        #             tasks.append(task)

        self.__dict__ = {k: v for k, v in {**defaults, **data}.items() if not k.startswith('_')}