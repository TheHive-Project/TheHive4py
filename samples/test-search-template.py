#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.query import Eq

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')

print('Search for case templates')
print('-----------------------------')

response = api.find_case_templates(query=Eq("status", "Ok"))

if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')

else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)
