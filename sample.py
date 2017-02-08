#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from TheHive4py.api import TheHiveApi
from TheHive4py.models import Case, CaseTask

api = TheHiveApi('http://localhost:9000', 'user', 'password')


# Prepare the sample case
tasks = [
    CaseTask(title='Tracking'),
    CaseTask(title='Communication')
]
tasks = []
case = Case(title='From TheHive4Py', tlp=3, flag=True, tags=['thehive4py', 'sample'], description='N/A', tasks=tasks)

# Create the case
print('Create Case')
print('-----------------------------')
id = None
response = api.create_case(case)
if(response.status_code == 200 or response.status_code == 201):
    print json.dumps(response.json(), indent=4, sort_keys=True)
    print('')
    id = response.json()['id']
else:
    print('ko: {}/{}'.format(response.status_code, response.text))

# Get all the details of the created case
print('Get created case {}'.format(id))
print('-----------------------------')
response = api.get_case(id)
if(response.status_code == requests.codes.ok):
    print json.dumps(response.json(), indent=4, sort_keys=True)
    print('')
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
