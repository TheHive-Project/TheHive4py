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

THEHIVE_URL = 'http://127.0.0.1:9000'
THEHIVE_API_KEY = '**YOUR_API_KEY**'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

# Prepare observables
inmemory_file = open('sample.txt', 'rb')
artifacts = [
    AlertArtifact(dataType='ip', data='8.8.8.8'),
    AlertArtifact(dataType='domain', data='google.com'),
    AlertArtifact(dataType='file', data='pic.png'),
    AlertArtifact(dataType='file', data=(inmemory_file, 'sample.txt'), sighted=True, ioc=True)
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
    customFields=customFields
)

# Create the alert
try:
  response = api.create_alert(alert)

  # Print the JSON response 
  print(json.dumps(response.json(), indent=4, sort_keys=True))

except AlertException as e:
  print("Alert create error: {}".format(e))

inmemory_file.close()

# Exit the program
sys.exit(0)
```

## Get an Alert by ID

Get an alert identified by `ALERT_ID` and display its title

```python
from thehive4py.api import TheHiveApi

THEHIVE_URL = 'http://127.0.0.1:9000'
THEHIVE_API_KEY = '**YOUR_API_KEY**'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

response = api.get_alert(ALERT_ID)

# Print alert title
alert_data = response.json()

print(alert_data.get('title'))
```

## Search alerts

Search for alerts with `HIGH` severity, `AMBER` TLP and with a title containing `MALSPAM`

```python

import json
from thehive4py.api import TheHiveApi
from thehive4py.models import *
from thehive4py.query import *

THEHIVE_URL = 'http://127.0.0.1:9000'
THEHIVE_API_KEY = '**YOUR_API_KEY**'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

query = And(
    Eq('tlp', Tlp.AMBER.value),
    Eq('severity', Severity.HIGH.value),
    Like('title', '*MALSPAM*')
)
response = api.find_alerts(query=query)

# Print the JSON response 
print(json.dumps(response.json(), indent=4, sort_keys=True))
```

## Promote an alert

Promote an alert identified by `ALERT_ID` to a case, using a case template named `MALSPAM`

```python
from thehive4py.api import TheHiveApi

THEHIVE_URL = 'http://127.0.0.1:9000'
THEHIVE_API_KEY = '**YOUR_API_KEY**'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

response = api.promote_alert_to_case(ALERT_ID, case_template='MALSPAM')
```
