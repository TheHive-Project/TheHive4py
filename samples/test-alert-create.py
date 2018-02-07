#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import requests
import sys
import json
import time
import uuid
from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, AlertArtifact

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')

artifacts = [
    AlertArtifact(dataType='ip', data='8.8.8.8'),
    AlertArtifact(dataType='domain', data='google.com'),
    AlertArtifact(dataType='file', data='pic.png'),
    AlertArtifact(dataType='file', data='sample.txt')
]


# Prepare the sample Alert
sourceRef = str(uuid.uuid4())[0:6]
alert = Alert(title='New Alert',
              tlp=3,
              tags=['TheHive4Py', 'sample'],
              description='N/A',
              type='external',
              source='instance1',
              sourceRef=sourceRef,
              artifacts=artifacts)

# Create the Alert
print('Create Alert')
print('-----------------------------')
id = None
response = api.create_alert(alert)
if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
    id = response.json()['id']
else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)


# Get all the details of the created alert
print('Get created alert {}'.format(id))
print('-----------------------------')
response = api.get_alert(id)
if response.status_code == requests.codes.ok:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')
else:
    print('ko: {}/{}'.format(response.status_code, response.text))