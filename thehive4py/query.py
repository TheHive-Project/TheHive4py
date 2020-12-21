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

A query is a defined by on of the criteria described below.

A query could be used like below:

```python
# Define the query
query = And(
    Eq('owner', 'admin'),
    Between('tlp', 1, 3),
    Not(Eq('status', 'Deleted')),
    Child('case_artifact', And(
        Eq('ioc', True),
        In('dataType', ['file', 'ip', 'domain'])
    ))
)

# Call find_cases method to search for all the case, sorted by descending created date, 
# and verifying the following set of conditions:
# - owned by admin
# - having tlp between GREEN and RED
# - not deleted
# - having observables of type file, ip or domain that are flagged as IOC

api.find_cases(query=query, sort=['-createdAt'], range='all')
```
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
    * search for customFields.cvss > 4.5
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
    * search for customFields.cvss >= 4.5
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
    * search for customFields.cvss < 4.5
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
    * search for customFields.cvss <= 4.5
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
    * search for closed cases related to customFields.customer "Company" and having a WHITE tlp

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
                And(
                    Eq('status', 'Open'),
                    Eq('flag', True),
                )
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
    A criterion used to search for records where `field` id defined. For example
    
    * search for cases that have the custom field `customer`

    Arguments:
        field (str): field name        

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for cases having a 'customer' custom field
            query = Contains('customFields.customer')
            ```
            produces
            ```json
            {
                "_contains": "customFields.customer"
            }
            ```
    """
    return {'_contains': field}


def Id(id):
    """
    A criterion used to search for records by id. For example
    
    * search for a case by its id
    * search for an alert by its id

    Arguments:
        id (str): the id's value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for as case by id
            query = Id('1234545643')
            ```
            produces
            ```json
            {
                "_id": "1234545643"
            }
            ```
    """
    return {'_id': id}


def Between(field, from_value, to_value):
    """
    A criterion used to search for records having `field`'s value included in a range defined by `from_value` and `to_value`. 
    This is an idea criterion to seahrch using date conditions. For example
    
    * search for cases created between two dates
    * search for alerts with cvss custom field greater that 2 and lesser than 9

    Arguments:
        field (str): field name
        from_value (Number): Lower limit of the range
        to_value (Number): Higher limit of the range

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for alerts with cvss custom field greater that 2 and lesser than 9
            query = Between('customFields.cvss.float', 2, 9)
            ```
            produces
            ```json
            {
                "_between": {
                    "_field": "customFields.cvss.float",
                    "_from": 2,
                    "_to": 9
                }
            }
            ```
    """
    return {'_between': {'_field': field, '_from': from_value, '_to': to_value}}


def ParentId(tpe, id):
    """
    A criterion used to search for records by their parent's id. For example
    
    * search for observables by case id
    * search for tasks by case id
    * search for logs by task id
    * search for jobs by observable id

    Arguments:
        tpe (str): class name of the parent: `case`, `case_task`, `case_artifact`...
        id (str): the parent id's value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for tasks of a case by id
            query = ParentId('case', '1234545643')
            ```
            produces
            ```json
            {
                "_parent": {
                    "_type": "case",
                    "_id": "1234545643"
                }
            }
            ```
    """
    return {'_parent': {'_type': tpe, '_id': id}}


def Parent(tpe, criterion):
    """
    A criterion used to search for records by filtering the parents using a criterion. For example
    
    * search for observables of TLP:RED cases
    * search for logs of tasks called 'Communication'

    Arguments:
        tpe (str): class name of the parent: `case`, `case_task`, `case_artifact`...
        criterion (Any): Any criterion defined by functions from the query module

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for tasks belonging to open cases with TLP=RED
            query = Parent('case', And(
                Eq('status', 'Open'),
                Eq('tlp', 3)
            ))
            ```
            produces
            ```json
            {
                "_parent": {
                    "_type": "case",
                    "_query": {
                        "_and": [
                            [
                                {
                                    "_field": "status",
                                    "_value": "Open"
                                },
                                {
                                    "_field": "tlp",
                                    "_value": 3
                                }
                            ]
                        ]
                    }
                }
            }
            ```
    """
    return {'_parent': {'_type': tpe, '_query': criterion}}


def Child(tpe, criterion):
    """
    A criterion used to search for records by applying a filter on their children using a criterion. For example
    
    * search for cases having file observables
    * search for cases having a specific ip observable

    Arguments:
        tpe (str): class name of the child: `case_task`, `case_artifact`...
        criterion (Any): Any criterion defined by functions from the query module

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for cases having iocs of type file
            query = Child('case_artifact', And(
                Eq('dataType', 'file'),
                Eq('ioc', True)
            ))
            ```
            produces
            ```json
            {
                "_child": {
                    "_type": "case_artifact",
                    "_query": {
                        "_and": [
                            [
                                {
                                    "_field": "dataType",
                                    "_value": "file"
                                },
                                {
                                    "_field": "ioc",
                                    "_value": true
                                }
                            ]
                        ]
                    }
                }
            }
            ```
    """
    return {'_child': {'_type': tpe, '_query': criterion}}


def Type(tpe):
    """
    A criterion used to search for records of the type defined by `tpe`. For example
    
    * search for objects of type 'audit'
    * search for objects of type 'alert'

    Arguments:
        tpe (str): object type's name as defined in TheHive: `all`, `case`, `case_task`, `case_task_log`, `case_artifact`, `alert`, `case_artifact_job`, `audit`

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for alerts
            query = Type('alert')
            ```
            produces
            ```json
            {
                "_type": "alert"
            }
            ```
    """
    return {'_type': tpe}


def String(query_string):
    """
    A criterion used to search for objects using Elasticsearch querystring syntax. For example
    
    * search for case using `title:misp AND tlp:2`

    Arguments:
        tpe (str): object type's name as defined in TheHive: 
            
            Possible values: `all`, `case`, `case_task`, `case_task_log`, `case_artifact`, `alert`, `case_artifact_job`, `audit`

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Query to search for casee with TLP:AMBER and having the word 'misp' on the title
            query = String('title:misp AND tlp:2')
            ```
            produces
            ```json
            {
                "_string": "title:misp AND tlp:2"
            }
            ```
    
    !!! Warning
        This criterion is deprecated and won't be ported to TheHive 4

    !!! Warning
        This criterion is available in TheHive 3 ONLY
    """
    return {'_string': query_string}


def Like(field, value):
    """
    A criterion used to search for objects having a text field's value like the specified `value`. 
    It's a wildcard operator when the searched value must specify asteriscs. For example:

    * search for cases where title is like `*malspam*`
    * search for observable where description contains the text `*malware*`

    Arguments:
        field (value): field name
        value (Any): searched value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Search for tasks where title contains 'Communication'
            query = Like('title', '*Communication*')
            ```
            produces
            ```json
            {
                "_like": {
                    "_field": "title",
                    "_value": "*Communication*"
                }
            }
            ```

    !!! Note
        If the `*` are not specified, the exact same text will be searched for.
        `Like('title', 'MISP')` will search for titles equal to `'MISP'`

    """
    return {'_like': {'_field': field, '_value': value}}


def StartsWith(field, value):
    """
    A criterion used to search for objects having a text field's value start with `value`. 
    It's a wildcard operator that adds the `*` if not specified, at the end of `value`. For example:

    * search for cases having a tag starting with `malspam`
    * search for filename observables starting with `dridex`

    Arguments:
        field (value): field name
        value (Any): searched value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Search for tasks where title stats with 'Communication'
            query = StartsWith('title', 'Communication')
            ```
            produces
            ```json
            {
                "_wildcard": {
                    "_field": "title",
                    "_value": "Communication*"
                }
            }
            ```
    """
    if not value.endswith('*'):
        value = value + '*'

    return {'_wildcard': {'_field': field, '_value': value}}


def EndsWith(field, value):
    """
    A criterion used to search for objects having a text field's value end with `value`. 
    It's a wildcard operator that adds the `*` if not specified, at the beginning of `value`. For example:

    * search for filename observables ending with `.exe`

    Arguments:
        field (value): field name
        value (Any): searched value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Search for tasks where title stats with 'Communication'
            query = EndsWith('data', '.png')
            ```
            produces
            ```json
            {
                "_wildcard": {
                    "_field": "data",
                    "_value": "*.png"
                }
            }
            ```
    """
    if not value.startswith('*'):
        value = '*' + value

    return {'_wildcard': {'_field': field, '_value': value}}


def ContainsString(field, value):
    """
    A criterion used to search for objects having a text field's value like the specified `value`. 
    It's a wildcard operator that wraps the searched value with asteriscs. It operates the same way a the `Like` criterion For example:

    * search for cases where title is like `*malspam*`
    * search for observable where description contains the text `*malware*`

    Arguments:
        field (value): field name
        value (Any): searched value

    Returns:
        dict: JSON repsentation of the criterion
            ```python
            # Search for tasks where title contains 'Communication'
            query = ContainsString('title', 'Communication')
            ```
            produces
            ```json
            {
                "_wildcard": {
                    "_field": "title",
                    "_value": "*Communication*"
                }
            }
            ```
    """
    if not value.endswith('*'):
        value = value + '*'

    if not value.startswith('*'):
        value = '*' + value

    return {'_wildcard': {'_field': field, '_value': value}}
