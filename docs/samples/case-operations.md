## Create a case

!!! missing
    TODO

## Get a case by ID

!!! missing
    TODO

## Find a case using few criteria

!!! missing
    TODO

## Search for cases

!!! missing
    TODO

## Update a case

An example showing how to update an case with custom fields.

```
import requests
import sys
import json
import time
import uuid
from thehive4py.api import TheHiveApi
from thehive4py.models import Case, CustomFieldHelper


THEHIVE_URL = 'http://127.0.0.1:9000'
THEHIVE_API_KEY = '**YOUR_API_KEY**'
ORGANISATION =  None                        # If you are using multiple orgs with same API_KEY, please specify the organisation, otherwise let it with the default value (None)

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY, ORGANISATION=ORGANISATION)


# Prepare custom fields
customFields = CustomFieldHelper()\
    .add_string('business-unit', 'HR')\
    .add_string('business-impact', 'HIGH')\
    .add_date('occur-date', int(time.time())*1000)\
    .add_number('cvss', 6)\
    .build()

# Prepare the sample Case with the fields to be updated with the new values - id field is mandatory
case_fields = Case(
    id = "~...",
    severity = 3,
    summary = "Summary of the case",
    customFields = customFields
    ...
)

# Update Case
try:
  response = api.update_case(case_fields, fields['severity', 'summary', 'customFields' ...])

  # Print the JSON response 
  print(json.dumps(response.json(), indent=4, sort_keys=True))

except CaseException as e:
  print("Case create error: {}".format(e))


# Exit the program
sys.exit(0)
```

## Search cases by observable

!!! missing
    TODO

## Close a case

!!! missing
    TODO
