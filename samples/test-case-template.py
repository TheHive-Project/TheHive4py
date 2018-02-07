#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CaseTemplate

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')

print('Create case from template')
print('-----------------------------')
case = Case(title='From TheHive4Py based on the Phishing template', description='N/A', tlp=2, template='Phishing')
print(case.jsonify())

print('Create Case')
print('-----------------------------')
response = api.create_case(case)
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
    id = response.json()['id']
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)
