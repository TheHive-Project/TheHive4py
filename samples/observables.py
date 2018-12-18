import json
import time
import uuid
import os

from thehive4py.api import Api
from thehive4py.models import Observable, Tlp
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
log('Case details by id', case.json(fields=['title', 'description']))

# Use the Tasks controller
observables = api.observables.of_case(case.id, Eq('dataType', 'ip'), range='0-1')
log('Case IPs', list(map(lambda i: i.json(), observables)))

observables = api.observables.of_type('ip', {}, range='0-10', sort=['-createdAt'])
log('Some IPs', list(map(lambda i: i.json(fields=['id', 'tags']), observables)))

# Prepare file
file_content = str(uuid.uuid4())
file_name = '{}.txt'.format(file_content)

file = open(file_name, 'w')
file.write(file_content)
file.close()

# Create file observable
file_observable = api.observables.create(case.id, Observable({
    'dataType': 'file',
    'data': file_name,
    'message': 'Sample from thehive4py',
    'tags': ['infected'],
    'ioc': True,
    'sighted': True
}))
log('New file observable', file_observable.json())

# Create file observable
mail_observable = api.observables.create(case.id, {
    'dataType': 'mail',
    'data': '{}@sample.com'.format(str(uuid.uuid4())[0:10]),
    'message': 'Sample from thehive4py',
    'tags': ['source'],
    'ioc': True,
    'sighted': True,
    'tlp': Tlp.WHITE.value
})
log('New mail observable', mail_observable.json())

api.observables.update(mail_observable.id, {
    'tags': ['source', 'src'],
    'ioc': False,
    'sighted': False,
    'tlp': Tlp.RED.value
})

# Clean up
os.remove(file_name)

# Run analyzer and responder
log('Run analyzer', api.observables.run_analyzer('local-cortex2', file_observable.id, 'FileInfo_5_0'))
log('Run responder', api.observables.run_responder('local-cortex2', file_observable.id, 'echoAnalyzer_1_0'))



