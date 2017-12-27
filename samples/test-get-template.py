#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseTemplate
from thehive4py.exceptions import CaseTemplateException

api = TheHiveApi('http://127.0.0.1:9000', 'username', 'password', {'http': '', 'https': ''})

print('Find existing case template')
print('-----------------------------')
template = api.get_case_template('Demo')
print(json.dumps(template, indent=4))

print('Find unknown case template')
print('-----------------------------')
try:
    template = api.get_case_template('Unknown')
    print(json.dumps(template, indent=4))
except CaseTemplateException as e:
    print(str(e))
