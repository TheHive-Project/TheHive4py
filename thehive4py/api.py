#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import sys

import magic
import os
import warnings
import json
import magic
import requests
from requests.auth import AuthBase

from thehive4py.models import CaseHelper
from thehive4py.query import *
from thehive4py.exceptions import *


class BasicAuth(AuthBase):
    """
        A custom authentication class for requests

        :param username: The username to use for the authentication
        :param password: The password to use for the authentication
        :param organisation: (Optional) The organisation to use
    """
    def __init__(self, username, password, organisation=None):
        self.username = username
        self.password = password
        self.organisation = organisation

    def __call__(self, req):
        req.headers['Authorization'] = requests.auth._basic_auth_str(self.username, self.password)

        if self.organisation is not None:
            req.headers['X-Organisation'] = self.organisation

        return req


class BearerAuth(AuthBase):
    """
        A custom authentication class for requests

        :param api_key: The API Key to use for the authentication
        :param organisation: (Optional) The organisation to use
    """
    def __init__(self, api_key, organisation=None):
        self.api_key = api_key
        self.organisation = organisation

    def __call__(self, req):
        req.headers['Authorization'] = 'Bearer {}'.format(self.api_key)

        if self.organisation is not None:
            req.headers['X-Organisation'] = self.organisation

        return req


class TheHiveApi:

    """
        Python API for TheHive

        :param url: thehive URL
        :param principal: The username or the API key
        :param password: The password for basic authentication or None. Defaults to None
        :param organisation: The organisation against which api calls will be run. Defaults to None
        :param proxies: The proxy configuration, would have `http` and `https` attributes. Defaults to {}
    """

    def __init__(self, url, principal, organisation=None, password=None, proxies={}, cert=True):

        self.url = url
        self.principal = principal
        self.password = password
        self.proxies = proxies
        self.organisation = organisation

        if self.password is not None:
            self.auth = BasicAuth(self.principal,self.password, self.organisation)
        else:
            self.auth = BearerAuth(self.principal, self.organisation)

        self.cert = cert

        # Create a CaseHelper instance
        self.case = CaseHelper(self)

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
            raise TheHiveException("Error: {}".format(e))

    def do_patch(self, api_url, **attributes):
        return requests.patch(self.url + api_url, headers={'Content-Type': 'application/json'}, json=attributes,
                              proxies=self.proxies, auth=self.auth, verify=self.cert)

    def health(self):
        req = self.url + "/api/health"
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise TheHiveException("Error on retrieving health status: {}".format(e))

    def get_current_user(self):
        req = self.url + "/api/user/current"
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise TheHiveException("Error on retrieving current user: {}".format(e))

    def create_case(self, case):

        """
        :param case: The case details
        :type case: Case defined in models.py
        :return: TheHive case
        :rtype: requests.Response
        """

        req = self.url + "/api/case"
        data = case.jsonify(excludes=['id'])
        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseException("Case create error: {}".format(e))

    def update_case(self, case, fields=[]):
        """
        Update a case.
        :param case: The case to update. The case's `id` determines which case to update.
        :param fields: Optional parameter, an array of fields names, the ones we want to update
        :return:
        """
        req = self.url + "/api/case/{}".format(case.id)

        # Choose which attributes to send
        update_keys = [
            'title', 'description', 'severity', 'startDate', 'owner', 'flag', 'tlp', 'pap', 'tags', 'status',
            'resolutionStatus', 'impactStatus', 'summary', 'endDate', 'metrics', 'customFields'
        ]
        data = {k: v for k, v in case.__dict__.items() if (len(fields) > 0 and k in fields) or (len(fields) == 0 and k in update_keys)}
        try:
            return requests.patch(req, headers={'Content-Type': 'application/json'}, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException:
            raise CaseException("Case update error: {}".format(e))

    def create_case_task(self, case_id, case_task):

        """
        :param case_id: Case identifier
        :param case_task: TheHive task
        :type case_task: CaseTask defined in models.py
        :return: TheHive task
        :rtype: requests.Response

        """

        req = self.url + "/api/case/{}/task".format(case_id)
        data = case_task.jsonify(excludes=['id'])

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case task create error: {}".format(e))

    def update_case_task(self, task, fields=[]):
        """
        :Updates TheHive Task
        :param case: The task to update. The task's `id` determines which Task to update.
        :return:
        """
        req = self.url + "/api/case/task/{}".format(task.id)

        # Choose which attributes to send
        update_keys = [
            'title', 'description', 'status', 'order', 'user', 'owner', 'flag', 'endDate'
        ]
        
        data = {k: v for k, v in task.__dict__.items() if (
            len(fields) > 0 and k in fields) or (len(fields) == 0 and k in update_keys)}

        try:
            return requests.patch(req, headers={'Content-Type': 'application/json'}, json=data,
                                  proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case task update error: {}".format(e))

    def create_task_log(self, task_id, case_task_log):

        """
        :param task_id: Task identifier
        :param case_task_log: TheHive log
        :type case_task_log: CaseTaskLog defined in models.py
        :return: TheHive log
        :rtype: requests.Response
        """

        req = self.url + "/api/case/task/{}/log".format(task_id)
        data = {'_json': json.dumps({"message": case_task_log.message})}

        if case_task_log.file:
            f = {'attachment': (os.path.basename(case_task_log.file), open(case_task_log.file, 'rb'), magic.Magic(mime=True).from_file(case_task_log.file))}
            try:
                return requests.post(req, data=data, files=f, proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                raise CaseTaskException("Case task log create error: {}".format(e))
        else:
            try:
                return requests.post(req, headers={'Content-Type': 'application/json'}, data=json.dumps({'message':case_task_log.message}), proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                raise CaseTaskException("Case task log create error: {}".format(e))

    def create_case_observable(self, case_id, case_observable):

        """
        :param case_id: Case identifier
        :param case_observable: TheHive observable
        :type case_observable: CaseObservable defined in models.py
        :return: TheHive observable
        :rtype: requests.Response
        """

        req = self.url + "/api/case/{}/artifact".format(case_id)

        if case_observable.dataType == 'file':
            try:
                mesg = json.dumps({
                    "dataType": case_observable.dataType,
                    "message": case_observable.message,
                    "tlp": case_observable.tlp,
                    "tags": case_observable.tags,
                    "ioc": case_observable.ioc,
                    "sighted": case_observable.sighted
                })
                data = {"_json": mesg}
                return requests.post(req, data=data, files=case_observable.data[0], proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                raise CaseObservableException("Case observable create error: {}".format(e))
        else:
            try:
                return requests.post(req, headers={'Content-Type': 'application/json'}, data=case_observable.jsonify(), proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                raise CaseObservableException("Case observable create error: {}".format(e))

    def update_case_observable(self, observable_id, case_observable):

        """
        :param observable_id: Observable identifier
        :param case_observable: TheHive observable
        :type case_observable: CaseObservable defined in models.py
        :return: TheHive observable
        :rtype: json
        """

        req = self.url + "/api/case/artifact/{}".format(observable_id)

        try:
            data = json.dumps({
                "message": case_observable.message,
                "tlp": case_observable.tlp,
                "tags": case_observable.tags,
                "ioc": case_observable.ioc,
                "sighted": case_observable.sighted
            })
            return requests.patch(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseObservableException("Case observable update error: {}".format(e))

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
            raise CaseException("Case fetch error: {}".format(e))

    def find_cases(self, **attributes):
        return self.__find_rows("/api/case/_search", **attributes)

    def delete_case(self, case_id, force=False):
        """
        Deletes a TheHive case. Unless force is set to True the case is 'soft deleted' (status set to deleted).
        :param case_id: Case identifier
        :return: A requests response object.
        """
        req = self.url + "/api/case/{}".format(case_id)
        if force:
            req += '/force'
        try:
            return requests.delete(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseException("Case deletion error: {}".format(e))

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
        parent_criteria = Parent('case', Id(case_id))

        # Append the custom query if specified
        if "query" in attributes:
            criteria = And(parent_criteria, attributes["query"])
        else:
            criteria = parent_criteria

        data = {
            "query": criteria
        }

        try:
            return requests.post(req, params=params, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseObservableException("Case observables search error: {}".format(e))

    def get_case_tasks(self, case_id, **attributes):
        req = self.url + "/api/case/task/_search"

        # Add range and sort parameters
        params = {
            "range": attributes.get("range", "all"),
            "sort": attributes.get("sort", [])
        }

        # Add body
        parent_criteria = Parent('case', Id(case_id))

        # Append the custom query if specified
        if "query" in attributes:
            criteria = And(parent_criteria, attributes["query"])
        else:
            criteria = parent_criteria

        data = {
            "query": criteria
        }

        try:
            return requests.post(req, params=params, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case tasks search error: {}".format(e))

    def get_linked_cases(self, case_id):
        """
        :param case_id: Case identifier
        :return: TheHive case(s)
        :rtype: json
        """
        req = self.url + "/api/case/{}/links".format(case_id)

        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseException("Linked cases fetch error: {}".format(e))

    def find_case_templates(self, **attributes):
        """
            :return: list of case templates
            :rtype: json
        """
        return self.__find_rows("/api/case/template/_search", **attributes)

    def get_case_template(self, name):

        """
        :param name: Case template name
        :return: TheHive case template
        :rtype: json

        """

        req = self.url + "/api/case/template/_search"
        data = {
            "query": And(Eq("name", name), Eq("status", "Ok"))
        }

        try:
            response = requests.post(req, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
            json_response = response.json()

            if response.status_code == 200 and len(json_response) > 0:
                return response.json()[0]
            else:
                raise CaseTemplateException("Case template fetch error: Unable to find case template {}".format(name))
        except requests.exceptions.RequestException as e:
            raise CaseTemplateException("Case template fetch error: {}".format(e))

    def create_case_template(self, case_template):

        """
        :param case_template: The case template
        :type case_template: CaseTemplate defined in models.py
        :return: TheHive case template
        :rtype: requests.Reponse
        """

        req = self.url + "/api/case/template"
        data = case_template.jsonify()

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTemplateException("Case template create error: {}".format(e))

    def _check_if_custom_field_exists(self, custom_field):
        data = {
                'key': 'reference',
                'value': custom_field.reference
            }
        req = self.url + "/api/list/custom_fields/_exists"
        response = requests.post(req, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        return response.json().get('found', 'False')

    def create_custom_field(self, custom_field):
        """
        This function is available only for TheHive 3

        :param custom_field: CustomField defined in models.py
        """

        if self._check_if_custom_field_exists(custom_field):
            raise CustomFieldException('Field with reference "{}" already exists'.format(custom_field.reference))

        data = {
            "value": {
                "name": custom_field.name,
                "reference": custom_field.reference,
                "description": custom_field.description,
                "type": custom_field.type,
                "options": custom_field.options,
                "mandatory": custom_field.madatory
                }
            }
        req = self.url + "/api/list/custom_fields"
        return requests.post(req, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)

    def get_case_task(self, task_id):
        """
        :param task_id: Task identifier
        :return: TheHive task by id
        :rtype: json
        """

        req = self.url + "/api/case/task/{}".format(task_id)
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case task logs search error: {}".format(e))

    def get_task_log(self, log_id):
        """
        :param log_id: Task log identifier
        :return: TheHive task log by id
        :rtype: json
        """

        req = self.url + "/api/case/task/log/{}".format(log_id)
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case task logs search error: {}".format(e))

    def get_task_logs(self, task_id):

        """
        :param task_id: Task identifier
        :return: TheHive logs
        :rtype: json
        """

        req = self.url + "/api/case/task/{}/log".format(task_id)
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case task logs search error: {}".format(e))

    def create_alert(self, alert):

        """
        :param alert: TheHive alert
        :type alert: Alert defined in models.py
        :return: TheHive alert
        :rtype: requests.Response
        """

        req = self.url + "/api/alert"
        data = alert.jsonify(excludes=['id'])
        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise AlertException("Alert create error: {}".format(e))

    def mark_alert_as_read(self, alert_id):
        """
        Mark an alert as read.
        :param alert_id: The ID of the alert to mark as read.
        :return:
        """
        req = self.url + "/api/alert/{}/markAsRead".format(alert_id)

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException:
            raise AlertException("Mark alert as read error: {}".format(e))

    def mark_alert_as_unread(self, alert_id):
        """
        Mark an alert as unread.
        :param alert_id: The ID of the alert to mark as unread.
        :return:
        """
        req = self.url + "/api/alert/{}/markAsUnread".format(alert_id)

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException:
            raise AlertException("Mark alert as unread error: {}".format(e))

    def update_alert(self, alert_id, alert, fields=[]):
        """
        Update an alert.
        :param alert_id: The ID of the alert to update.
        :param data: The alert to update.
        :param fields: Optional parameter, an array of fields names, the ones we want to update
        :return:
        """
        req = self.url + "/api/alert/{}".format(alert_id)

        # update only the alert attributes that are not read-only
        update_keys = ['tlp', 'severity', 'tags', 'caseTemplate', 'title', 'description', 'customFields']

        if len(fields) > 0:
            data = {k: v for k, v in alert.__dict__.items() if k in fields}
        else:
            data = {k: v for k, v in alert.__dict__.items() if k in update_keys}

        if hasattr(data, 'artifacts'):
            data['artifacts'] = [a.__dict__ for a in alert.artifacts]

        try:
            return requests.patch(req, headers={'Content-Type': 'application/json'}, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException:
            raise AlertException("Alert update error: {}".format(e))

    def get_alert(self, alert_id):
        """
            :param alert_id: Alert identifier
            :return: TheHive Alert
            :rtype: json
        """
        req = self.url + "/api/alert/{}".format(alert_id)

        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise AlertException("Alert fetch error: {}".format(e))

    def find_alerts(self, **attributes):
        """
            :return: list of Alerts
            :rtype: json
        """

        return self.__find_rows("/api/alert/_search", **attributes)

    def update_case_observables(self, observable, fields=[]):
        """
        :Updates TheHive observable
        :param observable: The observable details to update
        :return:
        """
        req = self.url + "/api/case/artifact/{}".format(observable.id)

        # Choose which attributes to send
        update_keys = ['tlp', 'ioc', 'flag', 'sighted', 'tags', 'message']

        data = {k: v for k, v in observable.__dict__.items() if (
            len(fields) > 0 and k in fields) or (len(fields) == 0 and k in update_keys)}

        try:
            return requests.patch(req, headers={'Content-Type': 'application/json'},
                json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case observable update error: {}".format(e))

    def promote_alert_to_case(self, alert_id, case_template=None):
        """
            This uses the TheHiveAPI to promote an alert to a case

            :param alert_id: Alert identifier
            :param case_template: Optional Case Template name
            :return: TheHive Case
            :rtype: json
        """

        req = self.url + "/api/alert/{}/createCase".format(alert_id)

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'},
                                 proxies=self.proxies, auth=self.auth,
                                 verify=self.cert, data=json.dumps({"caseTemplate": case_template}))

        except requests.exceptions.RequestException as the_exception:
            raise AlertException("Couldn't promote alert to case: {}".format(the_exception))

        return None

    def run_analyzer(self, cortex_id, artifact_id, analyzer_id):

        """
        :param cortex_id: identifier of the Cortex server
        :param artifact_id: identifier of the artifact as found with an artifact search
        :param analyzer_id: name of the analyzer used by the job
        :rtype: json
        """

        req = self.url + "/api/connector/cortex/job"

        try:
            data = json.dumps({ "cortexId": cortex_id,
                "artifactId": artifact_id,
                "analyzerId": analyzer_id
                })
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise TheHiveException("Analyzer run error: {}".format(e))

    def find_tasks(self, **attributes):
        """
            :return: list of Tasks
            :rtype: json
        """

        return self.__find_rows("/api/case/task/_search", **attributes)

# - addObservable(file)
# - addObservable(data)
