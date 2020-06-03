#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is a module that defines a set of utility methods used to easily build valid search query
without the need to use JSON objects.

Query objects are used by APIs that allow searchinf for objects like:

* [thehive4py.api.find_cases](./api#thehive4py.api.TheHiveApi.find_cases)
* [thehive4py.api.find_alerts](./api#thehive4py.api.TheHiveApi.find_alerts)
* [thehive4py.api.find_tasks](./api#thehive4py.api.TheHiveApi.find_tasks)

A query is a defined by criteria, described below
"""

def Eq(field, value):
    """
    A criterion used to search for a equality. For example

    * search for TLP = 2
    * search for flag = True
    * search for title = 'Sample case'

    Arguments:
        field (value): field name
        value (Any): field value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            query = Eq('tlp', 3)
            ```
            produces
            ```json
            {"_field": "tlp", "_value": 3}
            ```

    """
    return {'_field': field, '_value': value}


def Gt(field, value):
    """
    A criterion used to search for a field greater than a certain value. For example

    * search for TLP > 2
    * search for customField.cvss > 4.5
    * search for date > now

    Arguments:
        field (value): field name
        value (Any): field value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            query = Gt('tlp', 1)
            ```
            produces
            ```json
            {"_gt": {"tlp": 1}}
            ```
    """
    return {'_gt': {field: value}}


def Gte(field, value):
    """
    A criterion used to search for a field greater or equal than a certain value. For example

    * search for TLP >= 2
    * search for customField.cvss >= 4.5
    * search for date >= now

    Arguments:
        field (value): field name
        value (Any): field value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            query = Gte('tlp', 1)
            ```
            produces
            ```json
            {"_gte": {"tlp": 1}}
            ```
    """
    return {'_gte': {field: value}}


def Lt(field, value):
    """
    A criterion used to search for a field less than a certain value. For example

    * search for TLP < 2
    * search for customField.cvss < 4.5
    * search for date < now

    Arguments:
        field (value): field name
        value (Any): field value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            query = Lt('tlp', 3)
            ```
            produces
            ```json
            {"_lt": {"tlp": 3}}
            ```
    """
    return {'_lt': {field: value}}


def Lte(field, value):
    """
    A criterion used to search for a field less or equal than a certain value. For example

    * search for TLP <= 2
    * search for customField.cvss <= 4.5
    * search for date <= now

    Arguments:
        field (value): field name
        value (Any): field value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            query = Lte('tlp', 3)
            ```
            produces
            ```json
            {"_lte": {"tlp": 3}}
            ```
    """
    return {'_lte': {field: value}}


def And(*criteria):
    """
    A criterion used to search for a record using many criteria that must be true. For example

    * search for observables flagged as IOC and having TLP <= 2
    * search for closed cases related to customField.customer "Company" and having a WHITE tlp

    Arguments:
        criteria (Array): A set of criteria, one of the operator defined in the query module

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            query = And(
                Eq('customFields.customer.string', 'Company'), 
                Lte('tlp', 2), 
                Eq('status', 'Resolved')
            )
            ```
            produces
            ```json
            {
                "_and": [
                    {
                        "_field": "customFields.customer.string",
                        "_value": "Company"
                    },
                    {
                        "_lte": {
                            "tlp": 2
                        }
                    },
                    {
                        "_field": "status",
                        "_value": "Resolved"
                    }
                ]
            }
            ```
    """
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


def Like(field, value):
    return {'_like': {'_field': field, '_value': value}}


def StartsWith(field, value):
    if not value.endswith('*'):
        value = value + '*'

    return {'_wildcard': {'_field': field, '_value': value}}


def EndsWith(field, value):
    if not value.startswith('*'):
        value = '*' + value

    return {'_wildcard': {'_field': field, '_value': value}}


def ContainsString(field, value):

    if not value.endswith('*'):
        value = value + '*'

    if not value.startswith('*'):
        value = '*' + value

    return {'_wildcard': {'_field': field, '_value': value}}