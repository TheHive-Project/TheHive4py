#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

## Overview

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
    A criterion used to search for records that verfies all the specified criteria. For example

    * search for observables flagged as IOC and having TLP <= 2
    * search for closed cases related to customField.customer "Company" and having a WHITE tlp

    Arguments:
        criteria (Array): A set of criteria, can be any operator defined in the query module (`Eq`, `In`, `Not`, `And`...)

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for cases with customer custom field set to 'Company', having a TLP less than Amber and are resolved
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
    """
    A criterion used to search for records that verfies one of the specified criteria. For example

    * search for observables of type domain or fqdn
    * search for cases assigned to a given user or have a specific tag

    Arguments:
        criteria (Array): A set of criteria, can be any operator defined in the query module (`Eq`, `In`, `Not`, `And`...)

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for cases assigned to jdoe or are flagged and open
            query = Or(
                Eq('owner', 'jdoe'),
                And([
                    Eq('status', 'Open'),
                    Eq('flag', True),
                ])
            )
            ```
            produces
            ```json
            {
                "_or": [
                    {
                        "_field": "owner",
                        "_value": "jdoe"
                    },
                    {
                        "_and": [
                            [
                                {
                                    "_field": "status",
                                    "_value": "Open"
                                },
                                {
                                    "_field": "flag",
                                    "_value": true
                                }
                            ]
                        ]
                    }
                ]
            }
            ```
    """
    return {'_or': criteria}


def Not(criterion):
    """
    A criterion used to search for records that verfies the opposite of the specified criterion. For example

    * search for observables not marked as ioc
    * search for cases not having a MISP tag

    Arguments:
        crietrion (Any): The base criterion to use for negation

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for cases assigned to jdoe or are flagged and open
            query = Not(Eq('ioc', True))
            ```
            produces
            ```json
            {
                "_not": {
                    "_field": "ioc",
                    "_value": false
                }
            }
            ```
    """
    return {'_not': criterion}


def In(field, values):
    """
    A criterion used to search for records where `field` has one of the `values`. For example

    * search for observables of type domain, fqdn, ip
    * search for cases tagged as malspam, or phising

    Arguments:
        field (str): field name
        values (Array): A set of values the field must be in

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for observables of one of the following types: domain, fqdn, ip
            query = In('dataType', ['domain', 'fqdn', 'ip'])
            ```
            produces
            ```json
            {
                "_in": {
                    "_field": "dataType",
                    "_values": [
                        "domain",
                        "fqdn",
                        "ip"
                    ]
                }
            }
            ```
    """
    return {'_in': {'_field': field, '_values': values}}


def Contains(field):
    """
    !!! Warning
        TODO
    """
    return {'_contains': field}


def Id(id):
    """
    !!! Warning
        TODO
    """
    return {'_id': id}


def Between(field, from_value, to_value):
    """
    !!! Warning
        TODO
    """
    return {'_between': {'_field': field, '_from': from_value, '_to': to_value}}


def ParentId(tpe, id):
    """
    !!! Warning
        TODO
    """
    return {'_parent': {'_type': tpe, '_id': id}}


def Parent(tpe, criterion):
    """
    !!! Warning
        TODO
    """
    return {'_parent': {'_type': tpe, '_query': criterion}}


def Child(tpe, criterion):
    """
    !!! Warning
        TODO
    """
    return {'_child': {'_type': tpe, '_query': criterion}}


def Type(tpe):
    """
    !!! Warning
        TODO
    """
    return {'_type': tpe}


def String(query_string):
    """
    !!! Warning
        TODO
    """
    return {'_string': query_string}


def Like(field, value):
    """
    !!! Warning
        TODO
    """
    return {'_like': {'_field': field, '_value': value}}


def StartsWith(field, value):
    """
    !!! Warning
        TODO
    """
    if not value.endswith('*'):
        value = value + '*'

    return {'_wildcard': {'_field': field, '_value': value}}


def EndsWith(field, value):
    """
    !!! Warning
        TODO
    """
    if not value.startswith('*'):
        value = '*' + value

    return {'_wildcard': {'_field': field, '_value': value}}


def ContainsString(field, value):
    """
    !!! Warning
        TODO
    """
    if not value.endswith('*'):
        value = value + '*'

    if not value.startswith('*'):
        value = '*' + value

    return {'_wildcard': {'_field': field, '_value': value}}