#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import datetime
import json
import os
import time

from enum import Enum
import magic
import requests
from future.utils import raise_with_traceback

from thehive4py.exceptions import TheHiveException, CaseException


class Version(Enum):
    """
    Enumeration representing a version used to specify the version of TheHive instance

    Possible values: THEHIVE_3, THEHIVE_4
    """
    THEHIVE_3 = 3
    THEHIVE_4 = 4


class Tlp(Enum):
    """
    Enumeration representing TLP, used in cases, observables and alerts

    Possible values: WHITE, GREEN, AMBER, RED
    """
    WHITE = 0
    GREEN = 1
    AMBER = 2
    RED = 3


class Pap(Enum):
    """
    Enumeration representing PAP, used in cases, observables and alerts (TheHive 4 only)

    Possible values: WHITE, GREEN, AMBER, RED
    """
    WHITE = 0
    GREEN = 1
    AMBER = 2
    RED = 3


class Severity(Enum):
    """
    Enumeration representing severity, used in cases and alerts

    Possible values: LOW, MEDIUM, HIGH, CRITICAL
    """
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class CaseStatus(Enum):
    """
    Enumeration representing case statuses

    Possible values: OPEN, RESOLVED, DELETED, DUPLICATE
    """
    OPEN = 'Open'
    RESOLVED = 'Resolved'
    DELETED = 'Deleted'
    DUPLICATE = 'Duplicate'


class TaskStatus(Enum):
    """
    Enumeration representing task statuses

    Possible values: WAITING, INPROGRESS, COMPLETED, CANCEL
    """
    WAITING = 'Waiting'
    INPROGRESS = 'InProgress'
    COMPLETED = 'Completed',
    CANCEL = 'Cancel'


class CustomJsonEncoder(json.JSONEncoder):
    """
    Custom JSON encoder class that takes into account [thehive4py.models.JSONSerializable][] instances and 
    `datetime.datetime` objects
    """
    def default(self, o):
        """
        Method to serialize [thehive4py.models.JSONSerializable][] objects.

        Used by [thehive4py.models.JSONSerializable.jsonify][] method
        """
        if isinstance(o, JSONSerializable):
            return o.__dict__
        elif isinstance(o, datetime.datetime):
            return o.timestamp()
        else:
            return json.JSONEncoder.default(self, o)


class JSONSerializable(object):
    """
    Abstract class of all the models classes. 
    
    It defines utility methods called `jsonify` used to get a model object's JSON representation
    """

    def jsonify(self, excludes=[]):
        """
        A method that returns a stringyfied JSON representing a model object

        Arguments:
            excludes (str[]): list of fields to exclude from the returned JSON object.

        Returns:
            str: the JSON string of the object.
        """
        data = self.__dict__

        for ex in excludes:
            if ex in data:
                del data[ex]

        return json.dumps(data, sort_keys=True, indent=4, cls=CustomJsonEncoder)

    def attr(self, attributes, name, default, error=None):
        is_required = error is not None

        if is_required and name not in attributes:
            raise_with_traceback(ValueError(error))
        else:
            return attributes.get(name, default)


class CustomFieldHelper(object):
    """
    CustomFieldHelper
    """
    def __init__(self):
        self.fields = {}

    def __add_field(self, type, name, value):
        custom_field = dict()
        custom_field['order'] = len(self.fields)
        custom_field[type] = value
        self.fields[name] = custom_field

    def add_date(self, name, value):
        """
        Add a custom field of type `date`.

        Arguments:
            name (str): name of the custom field
            value (int): number of milliseconds representing a timestamp (Example: int(time.time())*1000)
        
        """
        self.__add_field('date', name, value)
        return self

    def add_string(self, name, value):
        """
        Add a custom field of type `string`.

        Arguments:
            name (str): name of the custom field
            value (str): value of the custom field
        
        """
        self.__add_field('string', name, value)
        return self

    def add_boolean(self, name, value):
        """
        Add a custom field of type `bool`.

        Arguments:
            name (str): name of the custom field
            value (bool): True or False, value of the custom field
        
        """
        self.__add_field('boolean', name, value)
        return self

    def add_number(self, name, value):
        """
        Add a custom field of type `number`.

        Arguments:
            name (str): name of the custom field
            value (number): value of the custom field
        
        !!! Warning
            This is method that work for TheHive 3 ONLY
        """
        self.__add_field('number', name, value)
        return self

    def add_integer(self, name, value):
        """
        Add a custom field of type `integer`.

        Arguments:
            name (str): name of the custom field
            value (int): value of the custom field
        
        !!! Warning
            This is method that work for TheHive 4 ONLY
        """
        self.__add_field('integer', name, value)
        return self

    def add_float(self, name, value):
        """
        Add a custom field of type `float`.

        Arguments:
            name (str): name of the custom field
            value (float): value of the custom field
        
        !!! Warning
            This is method that work for TheHive 4 ONLY
        """
        self.__add_field('float', name, value)
        return self

    def build(self):
        """
        Builds the custom field value dict as expected by TheHive, 
        maintining the order of the fields, specified by `order`

        Returns:
            dict: A json representation of the custom fields map
        """
        return self.fields


class CustomField(object):
    """
    Model class describing a custom field as defined in TheHive

    Arguments:
        name (str): name of the custom field
        reference (str): internal reference name
        description (str): description of the custom field
        type (Enum): type of the field, possible values are `string`, `boolean`, `number`, `date`, `integer`, `float`
        options (Any[]): list of possible values for the field
        mandatory (bool): True if the field is mandatory
    """

    def __init__(self, **attributes):
        self.name = attributes.get('name', None)
        self.reference = attributes.get('name', None)
        self.description = attributes.get('description', None)
        self.type = attributes.get('type', None)
        self.options = attributes.get('options', [])
        self.mandatory = attributes.get('mandatory', False)


class Case(JSONSerializable):
    """
    Model class describing a case as defined in TheHive

    Arguments:
        id (str): Case's id. Default: None
        title (str): Case's description. Default: None
        description (str): Case's description. Default: None
        tlp (Enum): Case's TLP: `0`, `1`, `2`, `3` for `WHITE`, `GREEN`, `AMBER`, `RED`. Default: `2`
        pap (Enum): Case's PAP: `0`, `1`, `2`, `3` for `WHITE`, `GREEN`, `AMBER`, `RED`. Default: `2`
        severity (Enum): Case's severity: `1`, `2`, `3`, `4` for `LOW`, `MEDIUM`, `HIGH`, `CRTICAL`. Default: `2`
        flag (bool): Case's flag, `True` to mark the case as important. Default: `False`
        tags (str[]): List of case tags. Default: `[]`
        startDate (datetime): Case's start date, the date the case occured. Default: `Now()`
        template (str): Case template's name. If specified then the case is created using the given template. Default: `None`
        owner (str): Case's assignee. Default: `None`
        metrics (JSON): Case metrics collection. A JSON object where keys are defining metric name, and values are defining metric value. Default: `{}`
        customFields (CustomField[]): A set of CustomField instances, or the result of a CustomFieldHelper.build() method. Default: `{}`
        tasks (JSON[] / CaseTask[]): Set of taks, defined either as JSON objects or CaseTask instances
        json (JSON): If the field is not equal to None, the case is instantiated using the JSON value instead of the arguements

    !!! Warning
        The `metrics` field is available in TheHive 3 only
    """
    def __init__(self, **attributes):
        defaults = {
            'id': None,
            'title': None,
            'description': None,
            'tlp': Tlp.AMBER.value,
            'pap': Pap.AMBER.value,
            'severity': Severity.MEDIUM.value,
            'flag': False,
            'tags': [],
            'startDate': int(time.time()) * 1000,
            'metrics': {},
            'customFields': {},
            'tasks': [],
            'template': None,
            'owner': None
        }

        if attributes.get('json', False):
            attributes = attributes['json']

        is_from_template = attributes.get('template', False)
        if is_from_template:
            defaults['template'] = attributes['template']

        self.id = attributes.get('id', None)
        self.title = attributes.get('title', None)
        self.description = attributes.get('description', defaults['description'])
        self.tlp = attributes.get('tlp', defaults['tlp'])
        self.pap = attributes.get('pap', defaults['pap'])
        self.severity = attributes.get('severity', defaults['severity'])
        self.flag = attributes.get('flag', defaults['flag'])
        self.tags = attributes.get('tags', defaults['tags'])
        self.startDate = attributes.get('startDate', defaults['startDate'])
        self.metrics = attributes.get('metrics', defaults['metrics'])
        self.customFields = attributes.get('customFields', defaults['customFields'])
        self.template = attributes.get('template', defaults['template'])
        self.owner = attributes.get('owner', defaults['owner'])

        tasks = attributes.get('tasks', defaults['tasks'])
        self.tasks = []
        for task in tasks:
            if type(task) == CaseTask:
                self.tasks.append(task)
            else:
                self.tasks.append(CaseTask(json=task))


class CaseHelper:
    """
    Provides helper methods for interacting with instances of the Case class.
    """
    def __init__(self, thehive):
        """
        Initialize a CaseHelper instance.
        :param thehive: A TheHiveApi instance.

        """
        self._thehive = thehive

    def __call__(self, id):
        """
        Return an instance of Case with the given case ID.
        :param id: ID of a case to retrieve.

        """
        response = self._thehive.get_case(id)

        # Check for failed authentication
        if response.status_code == requests.codes.unauthorized:
            raise TheHiveException("Authentication failed")

        if response.status_code == requests.codes.not_found:
            raise CaseException("Case {} not found".format(id))

        if self.status_ok(response.status_code):
            data = response.json()
            case = Case(json=data)

            # Add attributes that are not added by the constructor
            case.id = data.get('id', None)
            case.owner = data.get('owner', None)
            case.caseId = data.get('caseId', None)
            case.status = data.get('status', None)
            case.createdAt = data.get('createdAt', None)
            case.createdBy = data.get('createdBy', None)
            case.updatedAt = data.get('updatedAt', None)
            case.updatedBy = data.get('updatedBy', None)

            return case

    def create(self, title, description, **kwargs):
        """
        Create an instance of the Case class.
        :param title: Case title.
        :param description: Case description.
        :param kwargs: Additional arguments.

        :return: The created instance.

        """
        case = Case(title=title, description=description, **kwargs)
        response = self._thehive.create_case(case)

        # Check for failed authentication
        if response.status_code == requests.codes.unauthorized:
            raise TheHiveException("Authentication failed")

        if self.status_ok(response.status_code):
            return self(response.json()['id'])
        else:
            raise CaseException("Server returned {}: {}".format(response.status_code, response.text))

    def update(self, case_id, **attributes):
        """
        Update a case.
        :param case_id: The ID of the case to update
        :param attributes: key=value pairs of case attributes to update (field=new_value)

        :return: The created instance.
        """

        response = self._thehive.do_patch("/api/case/{}".format(case_id), **attributes)

        if response.status_code == requests.codes.unauthorized:
            raise TheHiveException("Authentication failed")

        if self.status_ok(response.status_code):
            return self(response.json()['id'])
        else:
            raise CaseException("Server returned {}: {}".format(response.status_code, response.text))

    @staticmethod
    def status_ok(status_code):
        """Check whether a status code is OK"""
        OK_STATUS_CODES = [200, 201]
        return status_code in OK_STATUS_CODES


class CaseTask(JSONSerializable):
    """
    Model class describing a case task as defined in TheHive

    Arguments:
        id (str): Task's id. Default: None
        title (str): Task's description. Default: None
        description (str): Task's description. Default: None
        status (Enum): Task's status: `Waiting`, `InProgress`, `Cancel`, `Completed`. Default: `Waiting`
        flag (bool): Task's flag, `True` to mark the Task as important. Default: `False`
        startDate (datetime): Task's start date, the date the task started at. Default: `None`
        owner (str): Task's assignee. Default: `None`
        json (JSON): If the field is not equal to None, the Task is instantiated using the JSON value instead of the arguements
    """

    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.id = attributes.get('id', None)
        self.title = attributes.get('title', None)
        self.status = attributes.get('status', TaskStatus.WAITING.value)
        self.flag = attributes.get('flag', False)
        self.description = attributes.get('description', None)
        self.owner = attributes.get('owner', None)
        self.startDate = attributes.get('startDate', None)
        self.group = attributes.get('group', None)


class CaseTaskLog(JSONSerializable):
    """
    Model class describing a case task log as defined in TheHive

    Arguments:
        id (str): Log's id. Default: None
        message (str): Log's description. Default: None
        file (str): Log attachment's path. If defined, the task log is created and the file is attached to it. Default: None
        json (JSON): If the field is not equal to None, the Task is instantiated using the JSON value instead of the arguements
    """
    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.id = attributes.get('id', None)
        self.message = attributes.get('message', None)
        self.file = attributes.get('file', None)

        if self.file is not None:
            if isinstance(self.file, tuple):
                file_object, filename = self.file
            else:
                filename = self.file
                # we are opening this here, but we can't close it
                # because it gets passed into requests.post. this is
                # the substance of issue #10.
                file_object = open(self.file, 'rb')

            mime = magic.Magic(mime=True).from_buffer(file_object.read())
            file_object.seek(0)
            self.attachment = {'attachment': (filename, file_object, mime)}
            

class CaseTemplate(JSONSerializable):
    """
    Model class describing a case template as defined in TheHive

    Arguments:
        id (str): Template's id. Default: None
        titlePrefix (str): Template's title prefix. Default: None
        description (str): Template's description. Default: None
        tlp (Enum): Template's TLP: `0`, `1`, `2`, `3` for `WHITE`, `GREEN`, `AMBER`, `RED`. Default: `2`
        pap (Enum): Template's PAP: `0`, `1`, `2`, `3` for `WHITE`, `GREEN`, `AMBER`, `RED`. Default: `2`
        severity (Enum): Template's severity: `1`, `2`, `3`, `4` for `LOW`, `MEDIUM`, `HIGH`, `CRTICAL`. Default: `2`
        flag (bool): Template's flag, `True` to mark the case as important when created from a template. Default: `False`
        tags (str[]): List of template tags. Default: `[]`
        metrics (JSON): Template metrics collection. A JSON object where keys are defining metric name, and values are defining metric value. Default: `{}`
        customFields (CustomField[]): A set of CustomField instances, or the result of a CustomFieldHelper.build() method. Default: `{}`
        tasks (JSON[] / CaseTask[]): Set of taks, defined either as JSON objects or CaseTask instances
        json (JSON): If the field is not equal to None, the template is instantiated using the JSON value instead of the arguements

    !!! Warning
        The `metrics` field is available in TheHive 3 only
    """

    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.id = attributes.get('id', None)
        self.name = attributes.get('name', None)
        self.id = attributes.get('id', None)
        self.titlePrefix = attributes.get('titlePrefix', None)
        self.description = attributes.get('description', None)
        self.severity = attributes.get('severity', Severity.MEDIUM.value)
        self.flag = attributes.get('flag', False)
        self.tlp = attributes.get('tlp', Tlp.AMBER.value)
        self.pap = attributes.get('pap', Pap.AMBER.value)
        self.tags = attributes.get('tags', [])
        self.metrics = attributes.get('metrics', {})
        self.customFields = attributes.get('customFields', {})

        tasks = attributes.get('tasks', [])
        self.tasks = []
        for task in tasks:
            if type(task) == CaseTask:
                self.tasks.append(task)
            else:
                self.tasks.append(CaseTask(json=task))


class CaseObservable(JSONSerializable):
    """
    Model class describing a case observable as defined in TheHive

    Arguments:
        id (str): Observable's id. Default: None
        dataType (str): Observable's type, must be a valid type, one of the defined data types in TheHive. Default: None
        message (str): Observable's description. Default: None
        tlp (Enum): Case's TLP: `0`, `1`, `2`, `3` for `WHITE`, `GREEN`, `AMBER`, `RED`. Default: `2`
        pap (Enum): Case's PAP: `0`, `1`, `2`, `3` for `WHITE`, `GREEN`, `AMBER`, `RED`. Default: `2`
        ioc (bool): Observable's ioc flag, `True` to mark an observable as IOC. Default: `False`
        sighted (bool): Observable's sighted flag, `True` to mark the observable as sighted. Default: `False`
        ignoreSimilarity (bool): Observable's similarity ignore flag. `True`to ignore the observable during similarity computing
        tags (str[]): List of observable tags. Default: `[]`
        data (str | (file, str)): Observable's data:

            - If the `dataType` field is set to `file`, then there are two options:

                * `data` must be equal to a string representing the file's path
                * `data` must be equal to Tuple composed by an in memory file object, and the file name

            - Otherwise, the `data` value is the observable's value
        json (JSON): If the field is not equal to None, the observable is instantiated using the JSON value instead of the arguements

    !!! Warning
        At least, one of `tags` or `message` are required. You cannot create an observable without specifying one of those fields

    !!! Warning
        `ignoreSimilarity` attribute is available in TheHive 4 ONLY
    """

    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.id = attributes.get('id', None)
        self.dataType = attributes.get('dataType', None)
        self.message = attributes.get('message', None)
        self.tlp = attributes.get('tlp', Tlp.AMBER.value)
        self.tags = attributes.get('tags', [])
        self.ioc = attributes.get('ioc', False)
        self.sighted = attributes.get('sighted', False)
        self.ignoreSimilarity = attributes.get('ignoreSimilarity', False)

        data = attributes.get('data', None)
        if self.dataType == 'file':
            if isinstance(data, tuple):
                file_object, filename = data
            else:
                filename = data
                # we are opening this here, but we can't close it
                # because it gets passed into requests.post. this is
                # the substance of issue #10.
                file_object = open(filename, 'rb')
            mime = magic.Magic(mime=True).from_buffer(file_object.read())
            file_object.seek(0)
            self.data = [{'attachment': (filename, file_object, mime)}]
        else:
            self.data = data


class Alert(JSONSerializable):
    """
    Model class describing an alert as defined in TheHive

    Arguments:
        id (str): Alert's id. Default: None
        tlp (Enum): Alert's TLP: `0`, `1`, `2`, `3` for `WHITE`, `GREEN`, `AMBER`, `RED`. Default: `2`
        pap (Enum): Alert's PAP: `0`, `1`, `2`, `3` for `WHITE`, `GREEN`, `AMBER`, `RED`. Default: `2` (TheHive 4 ONLY)
        severity (Enum): Alert's severity: `1`, `2`, `3`, `4` for `LOW`, `MEDIUM`, `HIGH`, `CRTICAL`. Default: `2`
        date (datetime): Alert's occur date. Default: `Now()`
        tags (str[]): List of alert tags. Default: `[]`

        title (str): Alert's description. Default: None
        type (str): Alert's type. Default: None
        source (str): Alert's source. Default: None
        sourceRef (str): Alert's source reference. Used to specify the unique identifier of the alert. Default: None
        externalLink (str): Alert's external link. Used to easily navigate to the source of the alert. Default: None
        description (str): Alert's description. Default: None
        customFields (CustomField[]): A set of CustomField instances, or the result of a CustomFieldHelper.build() method. Default: `{}`

        caseTemplate (str): Alert template's name. Default: `None`

        json (JSON): If the field is not equal to None, the Alert is instantiated using the JSON value instead of the arguements

    !!! Warning
            `pap`, `externalLink` attributes are available in TheHive 4 ONLY
    """

    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.id = attributes.get('id', None)
        self.tlp = attributes.get('tlp', Tlp.AMBER.value)
        self.pap = attributes.get('pap', Pap.AMBER.value)
        self.severity = attributes.get('severity', Severity.MEDIUM.value)
        self.date = attributes.get('date', int(time.time()) * 1000)
        self.tags = attributes.get('tags', [])
        self.caseTemplate = attributes.get('caseTemplate', None)
        self.externalLink = attributes.get('externalLink', None)

        self.title = self.attr(attributes, 'title', None, 'Missing alert title')
        self.type = self.attr(attributes, 'type', None, 'Missing alert type')
        self.source = self.attr(attributes, 'source', None, 'Missing alert source')
        self.sourceRef = self.attr(attributes, 'sourceRef', None, 'Missing alert reference')
        self.description = self.attr(attributes, 'description', None, 'Missing alert description')
        self.customFields = self.attr(attributes, 'customFields', {})

        artifacts = attributes.get('artifacts', [])
        self.artifacts = []
        for artifact in artifacts:
            if type(artifact) == AlertArtifact:
                self.artifacts.append(artifact.as_base64())
            else:
                self.artifacts.append(AlertArtifact(json=artifact).as_base64())


class AlertArtifact(JSONSerializable):
    """
    Model class describing a alert observable as defined in TheHive

    Arguments:
        dataType (str): Observable's type, must be a valid type, one of the defined data types in TheHive. Default: None
        message (str): Observable's description. Default: None
        tlp (Enum): Case's TLP: `0`, `1`, `2`, `3` for `WHITE`, `GREEN`, `AMBER`, `RED`. Default: `2`
        ioc (bool): Observable's ioc flag, `True` to mark an observable as IOC. Default: `False`
        sighted (bool): Observable's sighted flag, `True` to mark the observable as sighted. Default: `False`
        ignoreSimilarity (bool): Observable's similarity ignore flag. `True`to ignore the observable during similarity computing
        tags (str[]): List of observable tags. Default: `[]`
        data (str | (file, str)): Observable's data:

            - If the `dataType` field is set to `file`, then there are two options:

                * `data` must be equal to a string representing the file's path
                * `data` must be equal to Tuple composed by an in memory file object, and the file name

            - Otherwise, the `data` value is the observable's value
        json (JSON): If the field is not equal to None, the observable is instantiated using the JSON value instead of the arguements

    !!! Warning
        `ignoreSimilarity` attribute is available in TheHive 4 ONLY
    """

    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.dataType = attributes.get('dataType', None)
        self.message = attributes.get('message', None)
        self.tlp = attributes.get('tlp', Tlp.AMBER.value)
        self.tags = attributes.get('tags', [])
        self.ioc = attributes.get('ioc', False)
        self.sighted = attributes.get('sighted', False)

        if 'ignoreSimilarity' in attributes:
            self.ignoreSimilarity = attributes.get('ignoreSimilarity', False)

        data = attributes.get('data', None)
        if self.dataType != 'file':
            self.data = data
        else:
            if data is not None:
                if isinstance(data, tuple):
                    file_object, filename = data
                else:
                    filename = data
                    # we are opening this here, but we can't close it
                    # because it gets passed into requests.post. this is
                    # the substance of issue #10.
                    file_object = open(filename, 'rb')

                mime = magic.Magic(mime=True).from_buffer(file_object.read())
                file_object.seek(0)

                self.data = {'attachment': (filename, file_object, mime)}
            else:
                self.attachment = attributes.get('attachment', None)

    def as_base64(self):
        if 'data' in self.__dict__ and self.data is not None and self.dataType == 'file' and isinstance(self.data, dict):
            filename, file_object, mime = self.data.get('attachment')

            file_object.seek(0)
            encoded_string = base64.b64encode(file_object.read())

            self.data = "{};{};{}".format(filename, mime, encoded_string.decode())

        return self

