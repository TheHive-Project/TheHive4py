#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import sys
import json
from thehive4py.api import TheHiveApi

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


search("List Amber cases", {"_field": "tlp", "_value": 2}, 'all', [])
search("List White cases",
       {
            "_in": {
                "_field": "tlp",
                "_values": ["1", "3"]
            }
        },
       'all',
       ['+tlp']
)
search("Case of title containing 'TheHive4Py'", {"_string": "title:'TheHive4Py'"}, 'all', [])