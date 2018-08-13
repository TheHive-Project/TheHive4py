#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseTemplate
from thehive4py.exceptions import CaseTemplateException
from thehive4py.query import *

api = TheHiveApi('http://127.0.0.1:9000', 'JC7wGXWHi0XhvepKK1fBnP67d6JRjx0r')

print('Search for case templates')
print('-----------------------------')

response = api.find_case_templates(query=Eq("status", "Ok"))

if response.status_code == 200:
    print(json.dumps(response.json(), indent=4, sort_keys=True))
    print('')

else:
    print('ko: {}/{}'.format(response.status_code, response.text))
    sys.exit(0)
