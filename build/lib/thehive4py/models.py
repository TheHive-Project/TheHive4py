#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class CustomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, JSONSerializable):
            return o.__dict__
        else:
            return json.JSONEncoder.encode(self, o)


class JSONSerializable(object):
    # def __repr__(self):
    #     return json.dumps(self.__dict__)

    def jsonify(self):
        return json.dumps(self, sort_keys=True, cls=CustomJsonEncoder)
        # return json.dumps(self.__dict__)


class Case(JSONSerializable):

    def __init__(self, **attributes):
        self.title = attributes['title'] if attributes.get('title') else None
        self.description = attributes['description'] if attributes.get('description') else None
        self.tlp = attributes['tlp'] if attributes.get('tlp') else 2
        self.severity = attributes['severity'] if attributes.get('severity') else 2
        self.flag = attributes['flag'] if attributes.get('flag') else False
        self.tags = attributes['tags'] if attributes.get('tags') else []

        self.tasks = attributes['tasks'] if attributes.get('tasks') else []
        self.metrics = attributes['metrics'] if attributes.get('metrics') else {}


class CaseTask(JSONSerializable):

    def __init__(self, **attributes):
        self.title = attributes['title'] if attributes.get('title') else None
        self.status = attributes['status'] if attributes.get('status') else 'Waiting'
        self.flag = attributes['flag'] if attributes.get('flag') else False
        self.description = attributes['description'] if attributes.get('description') else None
        self.owner = attributes['owner'] if attributes.get('owner') else None
        self.startDate = attributes['startDate'] if attributes.get('startDate') else None
