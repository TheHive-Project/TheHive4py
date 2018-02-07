#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseObservable

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')

print('Create case')
print('-----------------------------')
case = Case(title='From TheHive4Py based on the Phishing template', description='N/A', tlp=2, tags=['thehive4py'])
print(case.jsonify())

response = api.create_case(case)
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
    id = response.json()['id']
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)


print('Create domain observable')
print('-----------------------------')
domain = CaseObservable(dataType='filename',
                        data=['pic.png'],
                        tlp=1,
                        ioc=True,
                        tags=['thehive4py'],
                        message='test'
                        )
response = api.create_case_observable(id, domain)
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)


print('Create file observable')
print('-----------------------------')
file_observable = CaseObservable(dataType='file',
                        data=['pic.png'],
                        tlp=1,
                        ioc=True,
                        tags=['thehive4py'],
                        message='test'
                        )
response = api.create_case_observable(id, file_observable)
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
    id = response.json()['id']
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)