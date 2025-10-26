import os
from tempfile import TemporaryDirectory

from thehive4py import TheHiveApi

hive = TheHiveApi(url="http://localhost:9000", apikey="h1v3b33")

case_to_enrich = hive.case.create(
    case={
        "title": "case to enrich",
        "description": "a case to enrich with task and task log",
    },
)

case_task_to_enrich = hive.task.create(
    case_id=case_to_enrich["_id"],
    task={"title": "a task to enrich with a task log and attachment"},
)

with TemporaryDirectory() as tmpdir:
    task_log_attachment_filepath = os.path.join(tmpdir, "task_log_attachment.txt")
    with open(task_log_attachment_filepath, "w") as attachment_file:
        attachment_file.write("attachment content")

    case_task_log = hive.task_log.create(
        task_id=case_task_to_enrich["_id"],
        task_log={
            "message": "a task log with an attachment",
            "attachments": [task_log_attachment_filepath],
        },
    )
