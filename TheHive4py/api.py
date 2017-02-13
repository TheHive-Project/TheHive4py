#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os
import re
import warnings

try:
    import requests
except Exception as excp:
    warnings.warn("requests library is non installed")


class TheHiveApi():

    """
        Python API for TheHive

        :param url: thehive URL
        :param username: username
        :param password: password
    """

    def __init__(self, url, username, password):

        self.url = url
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.auth = requests.auth.HTTPBasicAuth(username=self.username,
                                                password=self.password)

    def create_case(self, case):
        req = self.url + "/api/case"
        data = case.jsonify()
        return self.session.post(req, headers={'Content-Type': 'application/json'}, data=data, auth=self.auth)

    def create_case_task(self, id, caseTask):
        req = self.url + "/api/case/{}/task".format(id)
        data = caseTask.jsonify()
        return self.session.post(req, headers={'Content-Type': 'application/json'}, data=data, auth=self.auth)

    def create_task_log(self, taskId, caseTaskLog):
        req = self.url + "/api/case/task/{}/log".format(taskId)
        data = caseTaskLog.jsonify()
        return self.session.post(req, headers={'Content-Type': 'application/json'}, data=data, auth=self.auth)

    def get_case(self, id):
        req = self.url + "/api/case/{}".format(id)

        return self.session.get(req, auth=self.auth)

    def get_case_observables(self, id):
        req = self.url + "/api/case/artifact/_search"
        data = {
            "query": {
                "_and": [{
                    "_parent": {
                        "_type": "case",
                        "_query": {
                            "_id": id
                        }
                    }
                }, {
                    "status": "Ok"
                }]
            }
        }

        return self.session.post(req, json=data, auth=self.auth)


# - createCase()
# - createTask()
# - addLog()
# - addObservable(file)
# - addObservable(data)
