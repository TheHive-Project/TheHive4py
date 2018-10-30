import json
import time
import uuid
import os
from thehive4py.api import Api
from thehive4py.query import *


def log(title, result):
    print('------- {} --------'.format(title))
    if isinstance(result, dict) or isinstance(result, list):
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(result)


api = Api('http://localhost:9000', 'tBhBXMvsVJYrwcc6Qj9G9OE91m5a/PeF', proxies={
    'http': 'http://localhost:8080',
    'https': 'http://localhost:8080'
})

case = api.cases.get_by_number(143)
log('Case details by id', case.json())
log('Case details by id', case.json(fields=['title', 'description']))

# Use the Tasks controller
tasks = api.tasks.of_case(case.id, Eq('status', 'InProgress'), range='0-1')
log('Case tasks', list(map(lambda i: i.json(fields=['title', 'status', 'id']), tasks)))


# Prepare file
file_content = str(uuid.uuid4())
file_name = '{}.txt'.format(file_content)

file = open(file_name, 'w')
file.write(file_content)
file.close()

new_log = api.tasks.add_log(tasks[0].id, {
    'message': 'This is from TheHive4Py with attachment - **{}**'.format(str(uuid.uuid4())),
    'file': file_name
})

log('Run responder', api.tasklogs.run_responder('local-cortex2', new_log.id, 'echoAnalyzer_1_0'))

# Clean up
os.remove(file_name)

log('Case task log details', new_log.json())
log('Case task logs', list(map(lambda i: i.json(fields=['message', 'attachment']), api.tasks.get_logs(tasks[0].id, {}, range='all'))))

# Using TasklogsController
logs = api.tasklogs.find_all(tasks[0].id, Eq('owner', 'nabil'))
log('Case task logs', list(map(lambda i: i.json(fields=['message', 'attachment']), logs)))

log('Task log by id', api.tasklogs.get_by_id(logs[0].id))
new_log = api.tasklogs.create(tasks[0].id, {
    'message': 'This is from TheHive4Py with attachment - **{}**'.format(str(uuid.uuid4()))
})
api.tasklogs.remove(new_log.id)
