#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import time


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, JSONSerializable):
            return o.__dict__
        else:
            return json.JSONEncoder.encode(self, o)


class JSONSerializable(object):
    def jsonify(self):
        return json.dumps(self, sort_keys=True, indent=4, cls=CustomJsonEncoder)


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
            'metric': {},
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
        self.message = attributes.get('message', None)


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
