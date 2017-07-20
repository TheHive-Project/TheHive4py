#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import warnings
import json
import magic

try:
    import requests
except Exception as excp:
    warnings.warn("requests library is non installed")


class TheHiveApi:

    """
        Python API for TheHive

        :param url: thehive URL
        :param username: username
        :param password: password
    """

    def __init__(self, url, username, password, proxies, cert=True):

        self.url = url
        self.username = username
        self.password = password
        self.proxies = proxies
        self.auth = requests.auth.HTTPBasicAuth(username=self.username,
                                                password=self.password)
        self.cert = cert

    def create_case(self, case):

        """
        :param case: TheHive case
        :type case: Case defined in models.py
        :return: TheHive case
        :rtype: json
        """

        req = self.url + "/api/case"
        data = case.jsonify()
        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def create_case_task(self, caseId, caseTask):

        """
        :param caseId: Case identifier
        :param caseTask: TheHive task
        :type caseTask: CaseTask defined in models.py
        :return: TheHive task
        :rtype: json

        """

        req = self.url + "/api/case/{}/task".format(caseId)
        data = caseTask.jsonify()

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=True,)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def create_task_log(self, taskId, caseTaskLog):

        """
        :param taskId: Task identifier
        :param caseTaskLog: TheHive log
        :type caseTaskLog: CaseTaskLog defined in models.py
        :return: TheHive log
        :rtype: json
        """

        req = self.url + "/api/case/task/{}/log".format(taskId)
        data = {'_json': json.dumps({"message":caseTaskLog.message})}

        if caseTaskLog.file:
            f = {'attachment': ( os.path.basename(caseTaskLog.file), open(caseTaskLog.file, 'rb'), magic.Magic(mime=True).from_file(caseTaskLog.file))}
            try:
                return requests.post(req, data=data,files=f, proxies=self.proxies, auth=self.auth, verify=True)
            except requests.exceptions.RequestException as e:
                sys.exit("Error: {}".format(e))

        else:
            try:
                return requests.post(req, headers={'Content-Type': 'application/json'}, data=json.dumps({'message':caseTaskLog.message}), proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                sys.exit("Error: {}".format(e))

    def create_case_observable(self, caseId, caseObservable):

        """
        :param caseId: Case identifier
        :param caseObservable: TheHive observable
        :type caseObservable: CaseObservable defined in models.py
        :return: TheHive observable
        :rtype: json
        """

        req = self.url + "/api/case/{}/artifact".format(caseId)

        if caseObservable.dataType == 'file':
            try:
                mesg = json.dumps({ "dataType": caseObservable.dataType,
                    "message": caseObservable.message,
                    "tlp": caseObservable.tlp,
                    "tags": caseObservable.tags,
                    "ioc": caseObservable.ioc
                    })
                data = {"_json": mesg}
                return requests.post(req, data=data, files=caseObservable.data[0], proxies=self.proxies, auth=self.auth,verify=self.cert)
            except requests.exceptions.RequestException as e:
                    sys.exit("Error: {}".format(e))
        else:
            try:
                return requests.post(req, headers={'Content-Type': 'application/json'}, data=caseObservable.jsonify(), proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                    sys.exit("Error: {}".format(e))

    def get_case(self, caseId):
        """
            :param caseId: Case identifier
            :return: TheHive case
            :rtype: json
        """
        req = self.url + "/api/case/{}".format(caseId)

        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def find_cases(self, **attributes):

        """
            :return: list of observables
            :rtype: json
        """
        req = self.url + "/api/case/_search"

        # Add range and sort parameters
        params = {
            "range": attributes.get("range", "all"),
            "sort": attributes.get("sort", [])
        }

        # Add body
        data = {
            "query": attributes.get("query", "any")
        }

        try:
            return requests.post(req, json=data, proxies=self.proxies, auth=self.auth, params=params, verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def find_first(self, **attributes):
        """
            :return: first case of result set given by query
            :rtype: dict
        """
        return self.find_cases(**attributes).json()[0]

    def get_case_observables(self, caseId):

        """
        :param caseId: Case identifier
        :return: list of observables
        ;rtype: json
        """

        req = self.url + "/api/case/artifact/_search"
        data = {
            "query": {
                "_and": [{
                    "_parent": {
                        "_type": "case",
                        "_query": {
                            "_id": caseId
                        }
                    }
                }, {
                    "status": "Ok"
                }]
            }
        }

        try:
            return requests.post(req, json=data, proxies=self.proxies, auth=self.auth,verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def get_case_template(self, name):

        """
        :param name: Case template name
        :return: TheHive case template
        :rtype: json

        """

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
            response = requests.post(req, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
            jsonResponse = response.json()

            if response.status_code == 200 and len(jsonResponse) > 0:
                return response.json()[0]
            else:
                sys.exit("Error: {}".format("Unable to find case templates"))
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def get_case_tasks(self, caseId):
        req = self.url + "/api/case/task/_search?range=all"
        data = {
            'query': {
                '_parent': {
                    '_type': 'case',
                    '_query': {
                        '_id': caseId
                    }
                }
            }}
        try:
            response = requests.post(req, json=data, proxies=self.proxies, auth=self.auth)
            if response.status_code == 200 and len(response.json()) > 0:
                return response.json()
            else:
                sys.exit("Error: {}".format("Unable to find tasks"))
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def create_alert(self, alert):

        """
        :param alert: TheHive alert
        :type alert: Alert defined in models.py
        :return: TheHive alert
        :rtype: json
        """

        req = self.url + "/api/alert"
        data = alert.jsonify()
        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def get_alert(self, alert_id):
        """
            :param alert_id: Alert identifier
            :return: TheHive Alert
            :rtype: json
        """
        req = self.url + "/api/alert/{}".format(alert_id)

        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth,verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

# - addObservable(file)
# - addObservable(data)
