from thehive4py.query import *


def test_like():
    query = Like('name', 'thehive')

    assert '_like' in query
    assert '_field' in query['_like']
    assert '_value' in query['_like']

    assert query['_like']['_field'] == 'name'
    assert query['_like']['_value'] == 'thehive'


def test_startswith():
    query = StartsWith('name', 'thehive')

    assert '_wildcard' in query
    assert '_field' in query['_wildcard']
    assert '_value' in query['_wildcard']

    assert query['_wildcard']['_field'] == 'name'
    assert query['_wildcard']['_value'] == 'thehive*'


def test_endwith():
    query = EndsWith('name', 'thehive')

    assert '_wildcard' in query
    assert '_field' in query['_wildcard']
    assert '_value' in query['_wildcard']

    assert query['_wildcard']['_field'] == 'name'
    assert query['_wildcard']['_value'] == '*thehive'


def contains_string():
    query = ContainsString('name', 'thehive')

    assert '_wildcard' in query
    assert '_field' in query['_wildcard']
    assert '_value' in query['_wildcard']

    assert query['_wildcard']['_field'] == 'name'
    assert query['_wildcard']['_value'] == '*thehive*'
# query = And(Eq('status', 'Ok'), Eq('tlp', 2))
#
#
#
# print(json.dumps(query, indent=4, sort_keys=True))
#
# query = And(Parent('case', Id('XXXXXXXXXXXXXXx')), Eq('status', 'Ok'))
# print(json.dumps(query, indent=4, sort_keys=True))
