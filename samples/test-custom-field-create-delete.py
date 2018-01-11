#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import time
from thehive4py.api import TheHiveApi
from thehive4py.models import CustomFieldHelper

api = TheHiveApi('http://10.0.0.30:9000', 'oW60FLDIOzaAUnOh5+RX7x3dfYallLpA')

string_custom_field = CustomFieldHelper.create_new_field(
    'string',
    'Test String Custom Field',
    value=['First Option', 'Second Option', 'Third Option'],
    reference='testStringField',
    description='This is the description for the test string custom field')

print("Creating a string custom field")
creation_result = api.create_custom_field(string_custom_field)

if creation_result:
    print("ID: {}".format(creation_result))
    print("Sleeping for 30 seconds. Go check your custom fields for {}".format(string_custom_field['reference']))
    time.sleep(30)
else:
    print("could not create string custom field")
    exit()

print("Removing a string custom field")
deletion_result = api.delete_custom_field(creation_result)

if deletion_result:
    print("Deleted string custom field with ID {}".format(creation_result))
else:
    print("Could not delete string custom field with ID {}".format(creation_result))


boolean_custom_field = CustomFieldHelper.create_new_field(
        "boolean",
        "Was it bad?",
        reference="badPreference",
        description="Tell me if it was bad or not")

print("")
print("Creating a boolean custom field")
creation_result = api.create_custom_field(boolean_custom_field)

if creation_result:
    print("ID: {}".format(creation_result))
    print("Sleeping for 30 seconds. Go check your custom fields for {}".format(boolean_custom_field['reference']))
    time.sleep(30)
else:
    print("could not create boolean custom field")
    exit()

print("Removing a boolean custom field")
deletion_result = api.delete_custom_field(creation_result)

if deletion_result:
    print("Deleted boolean custom field with ID {}".format(creation_result))
else:
    print("Could not delete boolean custom field with ID {}".format(creation_result))