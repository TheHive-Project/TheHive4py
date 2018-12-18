from .model import Model


class Alert(Model):

    def __init__(self, data):
        defaults = {
            'title': None,
            'type': None,
            'source': None,
            'sourceRef': None,
            'description': None,
            'tlp': 2,
            'severity': 2,
            'date': None,
            'tags': [],
            'caseTemplate': None,
            'artifacts': [],
            'customFields': {}
        }

        if data is None:
            data = dict(defaults)

        self.__dict__ = {k: v for k, v in data.items() if not k.startswith('_')}


class AlertArtifact(Model):
    def __init__(self, input_data):
        defaults = {
            'dataType': None,
            'message': None,
            'tlp': 2,
            'tags': []
        }

        if input_data is None:
            input_data = dict(defaults)

        if 'dataType' in input_data and input_data['dataType'] == 'file':
            input_data['data'] = Model._prepare_file_data(input_data['data'])

        properties = {}
        properties.update(defaults)
        properties.update(input_data)

        self.__dict__ = {k: v for k, v in properties.items() if not k.startswith('_')}
