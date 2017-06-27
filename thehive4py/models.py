#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time
import os
import magic
import base64

from future.utils import raise_with_traceback


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, JSONSerializable):
            return o.__dict__
        else:
            return json.JSONEncoder.encode(self, o)


class JSONSerializable(object):
    def jsonify(self):
        return json.dumps(self, sort_keys=True, indent=4, cls=CustomJsonEncoder)

    def attr(self, attributes, name, default, error=None):
        is_required = error is not None

        if is_required and name not in attributes:
            raise_with_traceback(ValueError(error))
        else:
            return attributes.get(name, default)


class Case(JSONSerializable):

    def __init__(self, **attributes):
        defaults = {
            'title': None,
            'description': None,
            'tlp': 2,
            'severity': 2,
            'flag': False,
            'tags': [],
            'startDate': int(time.time()) * 1000,
            'metrics': {},
            'tasks': []
        }

        is_from_template = attributes.get('template', False)
        if is_from_template:
            template = attributes['template']
            defaults = {
                'title': None,
                'description': template.description,
                'tlp': template.tlp,
                'severity': template.severity,
                'flag': template.flag,
                'tags': template.tags,
                'startDate': int(time.time()) * 1000,
                'metrics': dict((el, None) for el in template.metricNames),
                'tasks': template.tasks
            }

        if attributes.get('json', False):
            attributes = attributes['json']

        if is_from_template:
            self.title = '[{}] {}'.format(template.titlePrefix, attributes.get('title', None)) if template.titlePrefix else attributes.get('title', None)
        else:
            self.title = attributes.get('title', None)

        self.description = attributes.get('description', defaults['description'])
        self.tlp = attributes.get('tlp', defaults['tlp'])
        self.severity = attributes.get('severity', defaults['severity'])
        self.flag = attributes.get('flag', defaults['flag'])
        self.tags = attributes.get('tags', defaults['tags'])
        self.startDate = attributes.get('startDate', defaults['startDate'])
        self.metrics = attributes.get('metrics', defaults['metrics'])

        tasks = attributes.get('tasks', defaults['tasks'])
        self.tasks = []
        for task in tasks:
            if type(task) == CaseTask:
                self.tasks.append(task)
            else:
                self.tasks.append(CaseTask(json=task))


class CaseTask(JSONSerializable):

    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.title = attributes.get('title', None)
        self.status = attributes.get('status', 'Waiting')
        self.flag = attributes.get('flag', False)
        self.description = attributes.get('description', None)
        self.owner = attributes.get('owner', None)
        self.startDate = attributes.get('startDate', None)


class CaseTaskLog(JSONSerializable):
    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.message = attributes.get('message', None)
        self.file = attributes.get('file', None)


class CaseTemplate(JSONSerializable):
    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.name = attributes.get('name', None)
        self.titlePrefix = attributes.get('titlePrefix', None)
        self.description = attributes.get('description', None)
        self.severity = attributes.get('severity', 2)
        self.flag = attributes.get('flag', False)
        self.tlp = attributes.get('tlp', 2)
        self.tags = attributes.get('tags', [])
        self.metricNames = attributes.get('metricNames', [])

        tasks = attributes.get('tasks', [])
        self.tasks = []
        for task in tasks:
            if type(task) == CaseTask:
                self.tasks.append(task)
            else:
                self.tasks.append(CaseTask(json=task))


class CaseObservable(JSONSerializable):
    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']
        self.dataType = attributes.get('dataType', None)
        self.message = attributes.get('message', None)
        self.tlp = attributes.get('tlp', 2)
        self.tags = attributes.get('tags', [])
        self.ioc = attributes.get('ioc', False)

        data = attributes.get('data', [])
        if self.dataType == 'file':
            self.data = [{'attachment': (os.path.basename(data[0]), open(data[0], 'rb'), magic.Magic(mime=True).from_file(data[0]))}]
        else:
            self.data = data


class Alert(JSONSerializable):
    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.tlp = attributes.get('tlp', 2)
        self.severity = attributes.get('severity', 3)
        self.date = attributes.get('date', int(time.time()) * 1000)
        self.tags = attributes.get('tags', [])
        self.caseTemplate = attributes.get('caseTemplate', None)

        self.title = self.attr(attributes, 'title', None, 'Missing alert title')
        self.type = self.attr(attributes, 'type', None, 'Missing alert type')
        self.source = self.attr(attributes, 'source', None, 'Missing alert source')
        self.sourceRef = self.attr(attributes, 'sourceRef', None, 'Missing alert reference')
        self.description = self.attr(attributes, 'description', None, 'Missing alert description')

        artifacts = attributes.get('artifacts', [])
        self.artifacts = []
        for artifact in artifacts:
            if type(artifact) == AlertArtifact:
                self.artifacts.append(artifact)
            else:
                self.artifacts.append(AlertArtifact(json=artifact))


class AlertArtifact(JSONSerializable):
    def __init__(self, **attributes):
        if attributes.get('json', False):
            attributes = attributes['json']

        self.dataType = attributes.get('dataType', None)
        self.message = attributes.get('message', None)
        self.tlp = attributes.get('tlp', 2)
        self.tags = attributes.get('tags', [])

        if self.dataType == 'file':
            self.data = self._prepare_file_data(attributes.get('data', None))
        else:
            self.data = attributes.get('data', None)

    def _prepare_file_data(self, file_path):
        with open(file_path, "rb") as file_artifact:
            filename = os.path.basename(file_path)
            mime = magic.Magic(mime=True).from_file(file_path)
            encoded_string = base64.b64encode(file_artifact.read())

        return "{};{};{}".format(filename, mime, encoded_string.decode())
