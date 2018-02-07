#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import json
import sys
import time

from thehive4py.api import TheHiveApi
from thehive4py.exceptions import CaseException
from thehive4py.models import CaseTask

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')


# Prepare the sample case
tasks = [
    CaseTask(title='Tracking'),
    CaseTask(title='Communication'),
    CaseTask(title='Investigation', status='Waiting', flag=True)
]
# tasks = []

# Create the case
print('Create Case')
print('-----------------------------')
case = None
try:
    case = thehive.case.create(title='From TheHive4Py', description='N/A', tlp=3, flag=True,
                           tags=['TheHive4Py', 'sample'], tasks=tasks)
except CaseException as e:
    print("Error creating case. {}".format(e))
    sys.exit(1)

# Print the details of the created case
print(case.jsonify())

# Add a new task to the created case
print('Add a task {}'.format(case.id))
print('-----------------------------')
response = thehive.create_case_task(case.id, CaseTask(
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
