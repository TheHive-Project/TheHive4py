#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import warnings
import json
import magic
import requests
from requests.auth import AuthBase


class BearerAuth(AuthBase):
    """
        A custom authentication class for requests

        :param api_key: The API Key to use for the authentication
    """
    def __init__(self, api_key):
        self.api_key = api_key

    def __call__(self, req):
        req.headers['Authorization'] = 'Bearer {}'.format(self.api_key)
        return req


class TheHiveApi:

    """
        Python API for TheHive

        :param url: thehive URL
        :param principal: The username or the API key
        :param password: The password for basic authentication or None. Defaults to None
    """

    def __init__(self, url, principal, password=None, proxies={}, cert=True):

        self.url = url
        self.principal = principal
        self.password = password
        self.proxies = proxies

        if self.password is not None:
            self.auth = requests.auth.HTTPBasicAuth(self.principal,self.password)
        else:
            self.auth = BearerAuth(self.principal)

        self.cert = cert

    def __find_rows(self, find_url, **attributes):
        """
            :param find_url: URL of the find api
            :type find_url: string
            :return: The Response returned by requests including the list of documents based on find_url
            :rtype: Response object
        """
        req = self.url + find_url

        # Add range and sort parameters
        params = {
            "range": attributes.get("range", "all"),
            "sort": attributes.get("sort", [])
        }

        # Add body
        data = {
            "query": attributes.get("query", {})
        }

        try:
            return requests.post(req, params=params, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def create_case(self, case):

        """
        :param case: The case details
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

    def create_case_task(self, case_id, case_task):

        """
        :param case_id: Case identifier
        :param case_task: TheHive task
        :type case_task: CaseTask defined in models.py
        :return: TheHive task
        :rtype: json

        """

        req = self.url + "/api/case/{}/task".format(case_id)
        data = case_task.jsonify()

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def create_task_log(self, task_id, case_task_log):

        """
        :param task_id: Task identifier
        :param case_task_log: TheHive log
        :type case_task_log: CaseTaskLog defined in models.py
        :return: TheHive log
        :rtype: json
        """

        req = self.url + "/api/case/task/{}/log".format(task_id)
        data = {'_json': json.dumps({"message":case_task_log.message})}

        if case_task_log.file:
            f = {'attachment': (os.path.basename(case_task_log.file), open(case_task_log.file, 'rb'), magic.Magic(mime=True).from_file(case_task_log.file))}
            try:
                return requests.post(req, data=data,files=f, proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                sys.exit("Error: {}".format(e))

        else:
            try:
                return requests.post(req, headers={'Content-Type': 'application/json'}, data=json.dumps({'message':case_task_log.message}), proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                sys.exit("Error: {}".format(e))

    def create_case_observable(self, case_id, case_observable):

        """
        :param case_id: Case identifier
        :param case_observable: TheHive observable
        :type case_observable: CaseObservable defined in models.py
        :return: TheHive observable
        :rtype: json
        """

        req = self.url + "/api/case/{}/artifact".format(case_id)

        if case_observable.dataType == 'file':
            try:
                mesg = json.dumps({ "dataType": case_observable.dataType,
                    "message": case_observable.message,
                    "tlp": case_observable.tlp,
                    "tags": case_observable.tags,
                    "ioc": case_observable.ioc
                    })
                data = {"_json": mesg}
                return requests.post(req, data=data, files=case_observable.data[0], proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                sys.exit("Error: {}".format(e))
        else:
            try:
                return requests.post(req, headers={'Content-Type': 'application/json'}, data=case_observable.jsonify(), proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                sys.exit("Error: {}".format(e))

    def get_case(self, case_id):
        """
            :param case_id: Case identifier
            :return: TheHive case
            :rtype: json
        """
        req = self.url + "/api/case/{}".format(case_id)

        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def find_cases(self, **attributes):
        return self.__find_rows("/api/case/_search", **attributes)

    def find_first(self, **attributes):
        """
            :return: first case of result set given by query
            :rtype: dict
        """
        return self.find_cases(**attributes).json()[0]

    def get_case_observables(self, case_id, **attributes):

        """
        :param case_id: Case identifier
        :return: list of observables
        ;rtype: json
        """

        req = self.url + "/api/case/artifact/_search"

        # Add range and sort parameters
        params = {
            "range": attributes.get("range", "all"),
            "sort": attributes.get("sort", [])
        }

        # Add body
        criteria = [{
            "_parent": {
                "_type": "case",
                "_query": {
                    "_id": case_id
                }
            }
        }, {
            "status": "Ok"
        }]

        # Append the custom query if specified
        if "query" in attributes:
            criteria.append(attributes["query"])

        data = {
            "query": {
                "_and": criteria
            }
        }

        try:
            return requests.post(req, params=params, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            sys.exit("Error: {}".format(e))

    def get_case_tasks(self, case_id, **attributes):
        req = self.url + "/api/case/task/_search"

        # Add range and sort parameters
        params = {
            "range": attributes.get("range", "all"),
            "sort": attributes.get("sort", [])
        }

        # Add body
        parent_criteria = {
            '_parent': {
                '_type': 'case',
                '_query': {
                    '_id': case_id
                }
            }
        }

        # Append the custom query if specified
        if "query" in attributes:
            criteria = {
                "_and": [
                    parent_criteria,
                    attributes["query"]
                ]
            }
        else:
            criteria = parent_criteria

        data = {
            "query": criteria
        }

        try:
            return requests.post(req, params=params, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
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
            json_response = response.json()

            if response.status_code == 200 and len(json_response) > 0:
                return response.json()[0]
            else:
                sys.exit("Error: {}".format("Unable to find case templates"))
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

    def find_alerts(self, **attributes):
        """
            :return: list of Alerts
            :rtype: json
        """

        return self.__find_rows("/api/alert/_search", **attributes)

# - addObservable(file)
# - addObservable(data)
