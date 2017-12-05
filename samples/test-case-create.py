#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import requests
import sys
import json
import time
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseTask, CustomFieldHelper

api = TheHiveApi('http://127.0.0.1:9000', 'username', 'password', {'http': '', 'https': ''})

# Prepare the sample case
tasks = [
    CaseTask(title='Tracking'),
    CaseTask(title='Communication'),
    CaseTask(title='Investigation', status='Waiting', flag=True)
]

# Prepare the custom fields
customFields = CustomFieldHelper()\
    .add_boolean('booleanField', True)\
    .add_string('businessImpact', 'HIGH')\
    .add_date('occurDate', int(time.time())*1000)\
    .add_number('cvss', 9)\
    .build()

case = Case(title='From TheHive4Py',
            tlp=3,
            flag=True,
            tags=['TheHive4Py', 'sample'],
            description='N/A',
            tasks=tasks,
            customFields=customFields)

# Create the case
print('Create Case')
print('-----------------------------')
id = None
response = api.create_case(case)
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
    id = response.json()['id']
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)

# Get all the details of the created case
print('Get created case {}'.format(id))
print('-----------------------------')
response = api.get_case(id)
if response.status_code == requests.codes.ok:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
else:
    print('ko: {}/{}'.format(response.status_code, response.text))

# Add a new task to the created case
print('Add a task {}'.format(id))
print('-----------------------------')
response = api.create_case_task(id, CaseTask(
    title='Yet Another Task',
    status='InProgress',
    owner='nabil',
    flag=True,
    startDate=int(time.time())*1000))
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
