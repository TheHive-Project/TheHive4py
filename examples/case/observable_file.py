import os.path
import tempfile

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

case_to_enrich = hive.case.create(
    case={
        "title": "case to enrich",
        "description": "a case to enrich with a file observable",
    }
)

with tempfile.TemporaryDirectory() as tmpdir:
    observable_filepath = os.path.join(tmpdir, "my-observable.txt")
    with open(observable_filepath) as observable_file:
        observable_file.write("some observable content")

    hive.case.create_observable(
        case_id=case_to_enrich["_id"],
        observable={"dataType": "file", "message": "a file based observable"},
        observable_path=observable_filepath,
    )
