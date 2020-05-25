import time
from thehive4py.models import CustomFieldHelper


def test_boolean():
    custom_fields = CustomFieldHelper() \
        .add_boolean('boolean-field', True) \
        .build()

    assert custom_fields is not None
    assert 'boolean-field' in custom_fields
    assert 'boolean' in custom_fields['boolean-field']
    assert 'order' in custom_fields['boolean-field']

    assert custom_fields['boolean-field']['boolean'] is True
    assert custom_fields['boolean-field']['order'] == 0


def test_date():
    date = int(time.time())*1000

    custom_fields = CustomFieldHelper() \
        .add_date('date-field', date) \
        .build()

    assert custom_fields is not None
    assert 'date-field' in custom_fields
    assert 'date' in custom_fields['date-field']
    assert 'order' in custom_fields['date-field']

    assert custom_fields['date-field']['date'] == date
    assert custom_fields['date-field']['order'] == 0


def test_string():
    custom_fields = CustomFieldHelper() \
        .add_string('string-field', 'thehive') \
        .build()

    assert custom_fields is not None
    assert 'string-field' in custom_fields
    assert 'string' in custom_fields['string-field']
    assert 'order' in custom_fields['string-field']

    assert custom_fields['string-field']['string'] == 'thehive'
    assert custom_fields['string-field']['order'] == 0


def test_number():
    custom_fields = CustomFieldHelper() \
        .add_number('number-field', 100) \
        .build()

    assert custom_fields is not None
    assert 'number-field' in custom_fields
    assert 'number' in custom_fields['number-field']
    assert 'order' in custom_fields['number-field']

    assert custom_fields['number-field']['number'] == 100
    assert custom_fields['number-field']['order'] == 0


def test_intger():
    custom_fields = CustomFieldHelper() \
        .add_integer('integer-field', 100) \
        .build()

    assert custom_fields is not None
    assert 'integer-field' in custom_fields
    assert 'integer' in custom_fields['integer-field']
    assert 'order' in custom_fields['integer-field']

    assert custom_fields['integer-field']['integer'] == 100
    assert custom_fields['integer-field']['order'] == 0


def test_intger():
    custom_fields = CustomFieldHelper() \
        .add_float('float-field', 1.0) \
        .build()

    assert custom_fields is not None
    assert 'float-field' in custom_fields
    assert 'float' in custom_fields['float-field']
    assert 'order' in custom_fields['float-field']

    assert custom_fields['float-field']['float'] == 1.0
    assert custom_fields['float-field']['order'] == 0


def test_order():
    custom_fields = CustomFieldHelper()\
        .add_boolean('booleanField', True)\
        .add_string('businessImpact', 'HIGH')\
        .add_date('occurDate', int(time.time())*1000)\
        .add_number('cvss', 9) \
        .add_integer('csirts', 2) \
        .add_float('hitRate', 50.2) \
        .build()

    assert custom_fields is not None
    assert 'booleanField' in custom_fields
    assert 'businessImpact' in custom_fields
    assert 'occurDate' in custom_fields
    assert 'cvss' in custom_fields
    assert 'csirts' in custom_fields
    assert 'hitRate' in custom_fields

    assert custom_fields['booleanField']['order'] == 0
    assert custom_fields['businessImpact']['order'] == 1
    assert custom_fields['occurDate']['order'] == 2
    assert custom_fields['cvss']['order'] == 3
    assert custom_fields['csirts']['order'] == 4
    assert custom_fields['hitRate']['order'] == 5


