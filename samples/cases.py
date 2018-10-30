import json
import time
from thehive4py.api import Api
from thehive4py.models import Case, Task, CustomFieldHelper
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

# Fetch cases
open_cases = api.cases.find_all({'status': 'Open'}, range='0-5')
log('Open cases', list(map(lambda i: i.json(), open_cases)))

# Fetch a case by `id` or `number` (caseId)
sample_case = open_cases[0]
log('case details by id', api.cases.get_by_id(sample_case.id).json())
log('case details by number', api.cases.get_by_number(sample_case.caseId).json())
log('case tasks', list(map(lambda i: i.json(), api.cases.get_tasks(sample_case.id, {}))))

case_by_observable = api.cases.has_observable({}, And(Eq('dataType', 'ip'), Eq('data', '8.8.8.8')), range='0-2')
log('case by observable', list(map(lambda i: i.json(), case_by_observable)))


# Prepare the custom fields
customFields = CustomFieldHelper()\
    .add_boolean('booleanField', True)\
    .add_string('businessImpact', 'HIGH')\
    .add_date('occurDate', int(time.time())*1000)\
    .add_number('cvss', 9)\
    .build()

new_case = api.cases.create(Case({
    'title': 'New Case from TH4P 2.0',
    'tlp': 2,
    'tags': ['TheHive4Py', 'sample'],
    'description': 'N/A',
    'customFields': customFields,
    'owner': 'nabil',
    'tasks': [
        {'title': 'Task 1'},
        {'title': 'Task 2', 'status': 'InProgress', 'startDate': int(time.time())*1000, 'owner': 'nabil'}
    ],
    'template': 'IOC',
}))
log('New case ', new_case.json())

api.cases.update(new_case.id, {'tlp': 1, 'severity': 1})

# Use the Tasks controller
log('case tasks', list(map(lambda i: i.json(), api.tasks.of_case(new_case.id, {}, range='0-3'))))
log('case waiting tasks', list(map(lambda i: i.json(), api.tasks.get_waiting({}, range='0-2'))))
log('case nabil\'s tasks', list(map(lambda i: i.json(), api.tasks.get_by_user('nabil', {}, range='0-2'))))

log('case nabil\'s tasks', list(map(lambda i: i.json(), api.tasks.get_logs('AWawpeJy_ejCJpgkGXRC', {}, range='0-2'))))


