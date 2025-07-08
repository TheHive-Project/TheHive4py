import os.path
import tempfile
import uuid

from thehive4py import TheHiveApi
from thehive4py.types.alert import InputAlert

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

with tempfile.TemporaryDirectory() as tmpdir:
    observable_filepath = os.path.join(tmpdir, "my-observable.txt")
    with open(observable_filepath, "w") as observable_file:
        observable_file.write("some observable content")

    attachment_key = uuid.uuid4().hex
    attachment_map = {attachment_key: observable_filepath}
    input_alert: InputAlert = {
        "type": "alert-with-file-observable",
        "source": "example",
        "sourceRef": uuid.uuid4().hex,
        "title": "alert with file observables",
        "description": "alert with file observables",
        "observables": [
            {"dataType": "file", "attachment": attachment_key},
        ],
    }

    hive.alert.create(alert=input_alert, attachment_map=attachment_map)
