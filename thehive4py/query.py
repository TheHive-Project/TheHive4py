#!/usr/bin/env python
# -*- coding: utf-8 -*-


def Eq(field, value):
    return {'_field': field, '_value': value}


def Gt(field, value):
    return {'_gt': {field: value}}


def Gte(field, value):
    return {'_gte': {field: value}}


def Lt(field, value):
    return {'_lt': {field: value}}


def Lte(field, value):
    return {'_lte': {field: value}}


def And(*criteria):
    return {'_and': criteria}


def Or(*criteria):
    return {'_or': criteria}


def Not(criterion):
    return {'_not': criterion}


def In(field, values):
    return {'_in': {'_field': field, '_values': values}}


def Contains(field):
    return {'_contains': field}


def Id(id):
    return {'_id': id}


def Between(field, from_value, to_value):
    return {'_between': {'_field': field, '_from': from_value, '_to': to_value}}


def ParentId(tpe, id):
    return {'_parent': {'_type': tpe, '_id': id}}


def Parent(tpe, criterion):
    return {'_parent': {'_type': tpe, '_query': criterion}}


def Child(tpe, criterion):
    return {'_child': {'_type': tpe, '_query': criterion}}


def Type(tpe):
    return {'_type': tpe}


def String(query_string):
    return {'_string': query_string}
