import os
import base64
import magic

from .model import Model


class Alert(Model):

    def __init__(self, data):
        defaults = {
            'id': None,
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
            input_data['data'] = AlertArtifact._prepare_file_data(input_data['data'])

        self.__dict__ = {k: v for k, v in {**defaults, **input_data}.items() if not k.startswith('_')}

    @staticmethod
    def _prepare_file_data(file_path):
        with open(file_path, 'rb') as file_artifact:
            filename = os.path.basename(file_path)
            mime = magic.Magic(mime=True).from_file(file_path)
            encoded_string = base64.b64encode(file_artifact.read())

        return "{};{};{}".format(filename, mime, encoded_string.decode())
