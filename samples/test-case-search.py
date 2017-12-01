#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.query import *

api = TheHiveApi('http://127.0.0.1:9000', 'username', 'password', {'http': '', 'https': ''})


def search(title, query, range, sort):
    print(title)
    print('-----------------------------')
    response = api.find_cases(query=query, range=range, sort=sort)

    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4, sort_keys=True))
        print('')
    else:
        print('ko: {}/{}'.format(response.status_code, response.text))
        sys.exit(0)


search("List Amber cases", Eq('tlp', 2), 'all', [])
search("List cases having some TLP values", In('tlp', [1, 3]), 'all', ['+tlp'])
search("Case of title containing 'TheHive4Py'", String("title:'TheHive4Py'"), 'all', [])
search("Closed cases, with tlp greater than or equal to Amber", And(Eq('status', 'Resolved'), Gte('tlp', 2), Gt('severity', 2)), '0-1', [])

