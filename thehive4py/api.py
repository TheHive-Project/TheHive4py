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

from thehive4py.auth import BasicAuth, BearerAuth
from thehive4py.models import CaseHelper
from thehive4py.query import Parent, Id, And, Eq
from thehive4py.exceptions import TheHiveException, CaseException, CaseTaskException, CaseTemplateException, AlertException, CaseObservableException, CustomFieldException


class TheHiveApi:

    def __init__(self, url: str, principal: str, password=None, proxies={}, cert=True, organisation=None):
        """
        Python API client for TheHive.

        Arguments:
            url (str): URL of Thehive instance, including the port. Ex: `http://myserver:9000`
            principal (str): The API key, or the username if basic authentication is used.
            password (str): The password for basic authentication or None. Defaults to None
            proxies (dict): The proxy configuration, would have `http` and `https` attributes. Defaults to {}
                ```python
                proxies: {
                    "http: "http://my_proxy:8080"
                    "https: "http://my_proxy:8080"
                }
                ```
            cert (bool): Wether or not to enable SSL certificate validation
            organisation (str): The name of the organisation against which api calls will be run. Defaults to None


        ??? note "Examples"
            === "Basic"
                Example of simple usage: call TheHive APIs using an API key, without proxy, nor organisation

                ```python
                api = TheHiveApi('http://my_thehive:9000', 'my_api_key')
                ```

            === "Full options"
                Example using all the options: call TheHive APIs using an API key, with orgnisation, proxy and sst certificate

                ```python
                proxies = {
                    "http: "http://my_proxy:8080"
                    "https: "http://my_proxy:8080"
                }
                api = TheHiveApi('http://my_thehive:9000',
                    'my_api_key',
                    proxies,
                    True,
                    'my-org'
                )
                ```
        """
        self.url = url
        self.principal = principal
        self.password = password
        self.proxies = proxies
        self.organisation = organisation

        if self.password is not None:
            self.auth = BasicAuth(self.principal, self.password, self.organisation)
        else:
            self.auth = BearerAuth(self.principal, self.organisation)

        self.cert = cert

        # Create a CaseHelper instance
        self.case = CaseHelper(self)

    def __find_rows(self, find_url, **attributes):
        """
        Private fuction that abstracts the calls to _search API

        Arguments:
            find_url: URL of the find api
            query (dict): A query object, defined in JSON format or using utiliy methods from thehive4py.query module
            sort (Array): List of fields to sort the result with. Prefix the field name with `-` for descending order
                and `+` for ascending order
            range (str): A range describing the number of rows to be returned

        Returns:
            response (requests.Response): Response object including a JSON array representing the list of searched records.

        Raises:
            TheHiveException
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
        """
        Method to call the /api/health endpoint

        Returns:
            Response object resulting from the API call.

        Raises:
            TheHiveException: Generic exception if an error occurs
        """
        req = self.url + "/api/health"
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise TheHiveException("Error on retrieving health status: {}".format(e))

    def get_current_user(self):
        """
        Method to call the /api/current endpoint, returning the current authenticated user.

        Returns:
            response (requests.Response): Response object including a JSON description of the current user

        Raises:
            TheHiveException: Generic exception if an error occurs
        """

        req = self.url + "/api/user/current"
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise TheHiveException("Error on retrieving current user: {}".format(e))

    def create_case(self, case):

        """
        Create a case

        Arguments:
            case (Case): Instance of [Case][thehive4py.models.Case]

        Returns:
            response (requests.Response): Response object including a JSON description of a case

        Raises:
            CaseException: An error occured during case creation
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

        Arguments:
            case (Case): Instance of [Case][thehive4py.models.Case] to update. The case's `id` determines which case to update.
            fields (Array): Optional parameter, an array of fields names, the ones we want to update

                Updatable fields are: [`title`, `description`, `severity`, `startDate`, `owner`, `flag`, `tlp`, `pap`, `tags`, `status`,
                `resolutionStatus`, `impactStatus`, `summary`, `endDate`, `metrics`, `customFields`]

        Returns:
            response (requests.Response): Response object including a JSON description of a case

        Raises:
            CaseException: An error occured during case creation
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
        except requests.exceptions.RequestException as e:
            raise CaseException("Case update error: {}".format(e))

    def create_case_task(self, case_id, case_task):

        """
        Create a case task

        Arguments:
            case_id: Case identifier
            case_task: Instance of [CaseTask][thehive4py.models.CaseTask]

        Returns:
            response (requests.Response): Response object including a JSON description of a case task

        Raises:
            CaseTaskException: An error occured during case task creation

        """

        req = self.url + "/api/case/{}/task".format(case_id)
        data = case_task.jsonify(excludes=['id'])

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case task create error: {}".format(e))

    def update_case_task(self, task, fields=[]):
        """
        Update a case task

        Arguments:
            task (CaseTask): Instance of [CaseTask][thehive4py.models.CaseTask]
            fields (array): Arry of strings representing CaseTask properties to be updated
               
                Updatable fields are: [`title`, `description`, `status`, `order`, `user`, `owner`, `flag`, `endDate`]

        Returns:
            response (requests.Response): Response object including a JSON description of a case task

        Raises:
            CaseTaskException: An error occured during case task creation
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
        Create a task log either with an attachement or just with a log message.

        Arguments:
            task_id (str): Task identifier
            case_task_log (CaseTaskLocg): Instance of [CaseTaskLog][thehive4py.models.CaseTaskLog]

        Returns:
            response (requests.Response): Response object including a JSON description of a case

        Raises:
            CaseException: An error occured during case creation
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
        Create a case observable

        Arguments:
            case_id (str): Case identifier
            case_observable (CaseObservable): Instance of [CaseObservable][thehive4py.models.CaseObservable]

        Returns:
            response (requests.Response): Response object including a JSON description of a case observable

        Raises:
            CaseObservableException: An error occured during case observable creation
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
                return requests.post(req, headers={'Content-Type': 'application/json'}, data=case_observable.jsonify(excludes=['id']), proxies=self.proxies, auth=self.auth, verify=self.cert)
            except requests.exceptions.RequestException as e:
                raise CaseObservableException("Case observable create error: {}".format(e))

    def update_case_observable(self, observable_id, case_observable):

        """
        Update an existing case observable

        Arguments:
            observable_id: Observable identifier
            case_observable (CaseObservable): Instance of [CaseObservable][thehive4py.models.CaseObservable]

        Returns:
            response (requests.Response): Response object including a JSON description of the updated case observable

        Raises:
            CaseObservableException: An error occured during case observable creation
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
        Get a case by id

        Arguments:
            case_id (str): Case identifier

        Returns:
            response (requests.Response): Response object including a JSON description of the case.

        Raises:
            CaseException: An error occured during case fetch
        """

        req = self.url + "/api/case/{}".format(case_id)

        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseException("Case fetch error: {}".format(e))

    def find_cases(self, **attributes):
        """
        Find cases using sort, pagination and a query

        Arguments:
            query (dict): A query object, defined in JSON format or using utiliy methods from thehive4py.query module
            sort (Array): List of fields to sort the result with. Prefix the field name with `-` for descending order
                and `+` for ascending order
            range (str): A range describing the number of rows to be returned

        Returns:
            response (requests.Response): Response object including a JSON array of cases.

        Raises:
            CaseException: An error occured during case search
        """
        return self.__find_rows("/api/case/_search", **attributes)

    def delete_case(self, case_id, force=False):
        """
        Deletes a TheHive case. Unless force is set to True the case is 'soft deleted' (status set to deleted).

        Arguments:
            case_id (str): Id of the case to delete
            force (bool): True to physically delete the case, False to mark the case as deleted

        Returns:
            response (requests.Response): Response object including true or false based on the action's success

        Raises:
            CaseException: An error occured during case deletion
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
        Find cases and return just the first record

        Arguments:
            query (dict): A query object, defined in JSON format or using utiliy methods from thehive4py.query module
            sort (Array): List of fields to sort the result with. Prefix the field name with `-` for descending order
                and `+` for ascending order
            range (str): A range describing the number of rows to be returned

        Returns:
            response (requests.Response): Response object including a JSON description of the case.

        Raises:
            CaseException: An error occured during case search
        """
        return self.find_cases(**attributes).json()[0]

    def get_case_observables(self, case_id, **attributes):

        """
        Find observables of a given case identified by its id

        Arguments:
            case_id (str): Id of the case
            query (dict): A query object, defined in JSON format or using utiliy methods from thehive4py.query module
            sort (Array): List of fields to sort the result with. Prefix the field name with `-` for descending order
                and `+` for ascending order
            range (str): A range describing the number of rows to be returned

        Returns:
            response (requests.Response): Response object including a JSON array of case observable.

        Raises:
            CaseObservableException: An error occured during case observable search
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
        """
        Find tasks of a given case identified by its id

        Arguments:
            case_id (str): Id of the case
            query (dict): A query object, defined in JSON format or using utiliy methods from thehive4py.query module
            sort (Array): List of fields to sort the result with. Prefix the field name with `-` for descending order
                and `+` for ascending order
            range (str): A range describing the number of rows to be returned

        Returns:
            response (requests.Response): Response object including a JSON array of case task.

        Raises:
            CaseTaskException: An error occured during case task search
        """

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
        Find related cases of a given case identified by its id

        Arguments:
            case_id (str): Id of the case

        Returns:
            response (requests.Response): Response object including a JSON array of related cases.

        Raises:
            CaseException: An error occured during case links fetch
        """
        req = self.url + "/api/case/{}/links".format(case_id)

        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseException("Linked cases fetch error: {}".format(e))

    def find_case_templates(self, **attributes):
        """
        Find case templates using a query, sort and pagination

        Arguments:
            query (dict): A query object, defined in JSON format or using utiliy methods from thehive4py.query module
            sort (Array): List of fields to sort the result with. Prefix the field name with `-` for descending order
                and `+` for ascending order
            range (str): A range describing the number of rows to be returned

        Returns:
            response (requests.Response): Response object including a JSON array of case templates

        Raises:
            TheHiveException: An error occured during case template search
        """
        return self.__find_rows("/api/case/template/_search", **attributes)

    def get_case_template(self, name):

        """
        Get a case template by its name

        Arguments:
            name (str): Case template's name

        Returns:
            response (requests.Response): Response object including a JSON representation of the case template

        Raises:
            CaseTemplateException: An error occured during case template fetch
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
        Create a case template

        Arguments:
            case_template (CaseTemplate): Instance of [CaseTemplate][thehive4py.models.CaseTemplate]

        Returns:
            response (requests.Response): Response object including a JSON representation of the case template

        Raises:
            CaseTemplateException: An error occured during case template creation
        """

        req = self.url + "/api/case/template"
        data = case_template.jsonify(excludes=['id'])

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
        Create a custom field

        Arguments:
            custom_field (CustomField): Instance of [CustomField][thehive4py.models.CustomField]

        Returns:
            response (requests.Response): Response object including a JSON representation of the case template

        Raises:
            CustomFieldException: Custom field already exists
            CustomFieldException: An error occured during custom field creation

        !!! Warning
            This function is available only for TheHive 3
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
        try:
            return requests.post(req, json=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CustomFieldException("Custom field create error: {}".format(e))

    def get_case_task(self, task_id):
        """
        Get a case task by its id

        Arguments:
            task_id (str): Case task identifier

        Returns:
            response (requests.Response): Response object including a JSON representation of the case task

        Raises:
            CaseTaskException: An error occured during case task fetch
        """

        req = self.url + "/api/case/task/{}".format(task_id)
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case task logs search error: {}".format(e))

    def get_task_log(self, log_id):
        """
        Get a case task log by its id

        Arguments:
            log_id (str): Case task log identifier

        Returns:
            response (requests.Response): Response object including a JSON representation of the case task log

        Raises:
            CaseTaskException: An error occured during case task log fetch
        """

        req = self.url + "/api/case/task/log/{}".format(log_id)
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case task logs search error: {}".format(e))

    def get_task_logs(self, task_id):
        """
        Get logs of a case task by its id

        Arguments:
            task_id (str): Case task identifier

        Returns:
            response (requests.Response): Response object including a JSON array representing a list of case task logs

        Raises:
            CaseTaskException: An error occured during case task log fetch
        """

        req = self.url + "/api/case/task/{}/log".format(task_id)
        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise CaseTaskException("Case task logs search error: {}".format(e))

    def create_alert(self, alert):

        """
        Create an alert. Supports adding observables and custom fields

        Arguments:
            alert (Alert): Instance of [Alert][thehive4py.models.Alert]

        Returns:
            response (requests.Response): Response object including a JSON array representing a list of case task logs

        Raises:
            AlertException: An error occured during alert creation
        """

        req = self.url + "/api/alert"
        data = alert.jsonify(excludes=['id'])
        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, data=data, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise AlertException("Alert create error: {}".format(e))

    def mark_alert_as_read(self, alert_id):
        """
        Mark an alert as read. This sets the status of the alert to `Ignored` if it's not yet promoted to a case.

        Arguments:
            alert_id (str): Id of the alert

        Returns:
            response (requests.Response): Response object including a JSON representation of the alert

        Raises:
            AlertException: An error occured during alert update
        """
        req = self.url + "/api/alert/{}/markAsRead".format(alert_id)

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise AlertException("Mark alert as read error: {}".format(e))

    def mark_alert_as_unread(self, alert_id):
        """
        Mark an alert as unread. This sets the status of the alert to `New` if it's not yet promoted to a case.

        Arguments:
            alert_id (str): Id of the alert

        Returns:
            response (requests.Response): Response object including a JSON representation of the alert

        Raises:
            AlertException: An error occured during alert update
        """
        req = self.url + "/api/alert/{}/markAsUnread".format(alert_id)

        try:
            return requests.post(req, headers={'Content-Type': 'application/json'}, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise AlertException("Mark alert as unread error: {}".format(e))

    def update_alert(self, alert_id, alert, fields=[]):
        """
        Update an alert completely or using specified fields

        Arguments:
            alert_id (str): Id of the alert
            alert (Alert): Instance of [Alert][thehive4py.models.Alert]
            fields (Array): Optional parameter, an array of field names, the ones we want to update

                Updatable fields are: [`tlp`, `severity`, `tags`, `caseTemplate`, `title`, `description`, `customFields`]

        Returns:
            response (requests.Response): Response object including a JSON representation of the alert

        Raises:
            AlertException: An error occured during alert update
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
        except requests.exceptions.RequestException as e:
            raise AlertException("Alert update error: {}".format(e))

    def get_alert(self, alert_id):
        """
        Get an alert by its id

        Arguments:
            alert_id (str): Id of the alert

        Returns:
            response (requests.Response): Response object including a JSON representation of the alert

        Raises:
            AlertException: An error occured during alert update
        """
        req = self.url + "/api/alert/{}".format(alert_id)

        try:
            return requests.get(req, proxies=self.proxies, auth=self.auth, verify=self.cert)
        except requests.exceptions.RequestException as e:
            raise AlertException("Alert fetch error: {}".format(e))

    def find_alerts(self, **attributes):
        """
        Find alerts using sort, pagination and a query

        Arguments:
            query (dict): A query object, defined in JSON format or using utiliy methods from thehive4py.query module
            sort (Array): List of fields to sort the result with. Prefix the field name with `-` for descending order
                and `+` for ascending order
            range (str): A range describing the number of rows to be returned

        Returns:
            response (requests.Response): Response object including a JSON array of alerts.

        Raises:
            AlertException: An error occured during alert search
        """

        return self.__find_rows("/api/alert/_search", **attributes)

    def update_case_observables(self, observable, fields=[]):
        """
        Update a case observable

        Arguments:
            observable (CaseObservable): Instance of [CaseObservable][thehive4py.models.CaseObservable] to update. 
                The observable's `id` determines which case to update.
            fields (Array): Optional parameter, an array of fields names, the ones we want to update.
                
                Updatable fields are: [`tlp`, `ioc`, `flag`, `sighted`, `tags`, `message`]

        Returns:
            response (requests.Response): Response object including a JSON description of a case observable

        Raises:
            CaseObservableException: An error occured during observable update
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
        Create a new case from an alert, with an optional case template

        Arguments:
            alert_id (str): Id of the alert
            case_template (str): Case template name to apply when creating the cas
            
        Returns:
            response (requests.Response): Response object including a JSON representation of the alert

        Raises:
            AlertException: An error occured during alert promotion
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
        Create a new case from an alert, with an optional case template

        Arguments:
            cortex_id: identifier of the Cortex server
            artifact_id: identifier of the artifact as found with an artifact search
            analyzer_id: name of the analyzer used by the job
            
        Returns:
            response (requests.Response): Response object including a JSON representation of the analysis job

        Raises:
            TheHiveException: An error occured during job creation
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
        Find case tasks using sort, pagination and a query

        Arguments:
            query (dict): A query object, defined in JSON format or using utiliy methods from thehive4py.query module
            sort (Array): List of fields to sort the result with. Prefix the field name with `-` for descending order
                and `+` for ascending order
            range (str): A range describing the number of rows to be returned

        Returns:
            response (requests.Response): Response object including a JSON array of case tasks.

        Raises:
            AlertException: An error occured during case task search
        """

        return self.__find_rows("/api/case/task/_search", **attributes)

# - addObservable(file)
# - addObservable(data)
