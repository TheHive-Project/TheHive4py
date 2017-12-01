#!/usr/bin/env python
# -*- coding: utf-8 -*-

from thehive4py.api import TheHiveApi


thehive = TheHiveApi('http://127.0.0.1:9000', 'username', 'password', {'http': '', 'https': ''})

# Create a new case
case = thehive.case.create(title='From TheHive4Py', description='N/A', tlp=3, flag=True,
                           tags=['TheHive4Py', 'sample'], tasks=[])

# Save the new case's ID for later use
case_id = case.id

# Change some attributes of the new case
case.tlp = 1
case.severity = 1
case.flag = False

# Update the case
thehive.update_case(case)

# Retrieve the case from the server and check the updated values
new_case = thehive.case(case_id)
print("Case ID {}\nTLP: {}, Severity: {}".format(new_case.id, new_case.tlp, new_case.severity))