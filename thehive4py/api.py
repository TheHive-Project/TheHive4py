#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
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

    def __init__(self, url, username, password, proxies):

        self.url = url
        self.username = username
        self.password = password
        self.proxies = proxies
        self.session = requests.Session()
        self.auth = requests.auth.HTTPBasicAuth(username=self.username,
                                                password=self.password)

    def create_case(self, case):
        req = self.url + "/api/case"
        data = case.jsonify()
        try:
            return self.session.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def create_case_task(self, id, caseTask):
        req = self.url + "/api/case/{}/task".format(id)
        data = caseTask.jsonify()

        try:
            return self.session.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def create_task_log(self, taskId, caseTaskLog):
        req = self.url + "/api/case/task/{}/log".format(taskId)
        data = caseTaskLog.jsonify()

        try:
            return self.session.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def get_case(self, id):
        req = self.url + "/api/case/{}".format(id)

        try:
            return self.session.get(req, proxies=self.proxies, auth=self.auth)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))
            
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

        try:
            return self.session.post(req, json=data, proxies=self.proxies, auth=self.auth)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def get_case_template(self, name):
        req = self.url + "/api/case/template/_search"
        data = {
            "query": {
                "_and": [{
                    "_field": "name",
                    "_value": name
                }, {
                    "status": "Ok"
                }]
            }
        }

        try:
            response = self.session.post(req, json=data, proxies=self.proxies, auth=self.auth)
            jsonResponse = response.json()

            if response.status_code == 200 and len(jsonResponse) > 0:
                return response.json()[0]
            else:
                sys.exit("Error: {}".format("Unable to find case templates"))
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))
            

# - createCase()
# - createTask()
# - addLog()
# - addObservable(file)
# - addObservable(data)
