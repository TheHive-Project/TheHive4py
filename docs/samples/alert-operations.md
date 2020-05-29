## Create alert

An example showing how to create an alert with observables and custom fields.

```python
import requests
import sys
import json
import time
import uuid
from thehive4py.api import TheHiveApi
from thehive4py.models import Alert, AlertArtifact, CustomFieldHelper

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')

# Prepare observables
artifacts = [
    AlertArtifact(dataType='ip', data='8.8.8.8'),
    AlertArtifact(dataType='domain', data='google.com'),
    AlertArtifact(dataType='file', data='pic.png'),
    AlertArtifact(dataType='file', data='sample.txt', sighted=True, ioc=True)
]

# Prepare custom fields
customFields = CustomFieldHelper()\
    .add_string('business-unit', 'HR')\
    .add_string('business-impact', 'HIGH')\
    .add_date('occur-date', int(time.time())*1000)\
    .add_number('cvss', 6)\
    .build()

# Prepare the sample Alert
sourceRef = str(uuid.uuid4())[0:6]
alert = Alert(title='New Alert',
              tlp=3,
              tags=['TheHive4Py', 'sample'],
              description='N/A',
              type='external',
              source='instance1',
              sourceRef=sourceRef,
              artifacts=artifacts,
              customFields=customFields)

# Create the alert
try:
  response = api.create_alert(alert)

  # Print the JSON response 
  print(json.dumps(response.json(), indent=4, sort_keys=True))

except AlertException as e:
  print("Alert create error: {}".format(e))

# Exit the program
sys.exit(0)
```

## Get an Alert by ID

!!! missing
    TODO

## Search alerts

!!! missing
    TODO

## Promote an alert

!!! missing
    TODO