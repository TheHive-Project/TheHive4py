#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from thehive4py.api import TheHiveApi
import json

api = TheHiveApi('http://localhost:9000', '**YOUR_API_KEY**')

# Update the case by ID
print('Update Case')
print('-----------------------------')

try:
    updated_case = api.case.update('AWFTw7pcX9h1rajWeETC',
                                   status='Resolved',
                                   resolutionStatus='TruePositive',
                                   impactStatus='NoImpact',
                                   summary='closed by api',
                                   tags=['test'])

    # Print the details of the updated case
    print(updated_case.jsonify())
except CaseException as e:
    print("Error updating case. {}".format(e))