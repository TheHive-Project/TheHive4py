#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi

ALERT_ID = '** PUT AN ALERT ID HERE **'
API_KEY = '** YOUR API KEY **'

api = TheHiveApi('http://127.0.0.1:9000', API_KEY)

print('Promoting alert %s to a case' % ALERT_ID)
print('-----------------------------')

response = api.promote_alert_to_case(ALERT_ID)

if response.status_code == 201:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')

else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)
