import json
import os
import base64
import magic


class Model(object):
    def __str__(self):
        return json.dumps(self.__dict__, indent=2)

    def json(self, **kwargs):
        fields = kwargs.get('fields', [])

        if len(fields) > 0:
            return {k: v for k, v in self.__dict__.items() if k in fields}
        else:
            return self.__dict__

    @staticmethod
    def _prepare_file_data(file_path):
        with open(file_path, 'rb') as file_artifact:
            filename = os.path.basename(file_path)
            mime = magic.Magic(mime=True).from_file(file_path)
            encoded_string = base64.b64encode(file_artifact.read())

        return "{};{};{}".format(filename, mime, encoded_string.decode())
