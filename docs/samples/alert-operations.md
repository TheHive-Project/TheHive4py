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

## Update alert

Update an existing alert

```python
from thehive4py.api import TheHiveApi

THEHIVE_URL = 'http://127.0.0.1:9000'
THEHIVE_API_KEY = '**YOUR_API_KEY**'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

response = api.get_alert(ALERT_ID)

# Update description
alert_data = response.json()
alert_data['description'] = 'Updated alert desciption...'

# Update alert
api.update_alert(alert=Alert(json=alert_data), alert_id=ALERT_ID, fields=['description'])
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

## Create an Alert Artifact

Create and add an artifact to an existing alert identified by `ALERT_ID`

!!! Warning
    This function is available in TheHive 4 ONLY
    
```python
from thehive4py.api import TheHiveApi
from thehive4py.models import Tlp

THEHIVE_URL = 'http://127.0.0.1:9000'
THEHIVE_API_KEY = '**YOUR_API_KEY**'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

# Instanciate a new domain artifact
artifact = AlertArtifact(dataType='domain', data='malicious-domain.tld', ignoreSimilarity=True, ioc=True)
api.create_alert_artifact(ALERT_ID, artifact)

# Instanciate a new file artifact
artifact = AlertArtifact(
    dataType='file', 
    data='malicious-file.exe', 
    ignoreSimilarity=False, 
    ioc=True, 
    sighted=True, 
    tlp=Tlp.RED.value)
api.create_alert_artifact(alert_id, artifact)
```

## Update an Alert Artifact

Update an existing artifact identified by `ALERT_ID`

!!! Warning
    This function is available in TheHive 4 ONLY
    
```python
from thehive4py.api import TheHiveApi
from thehive4py.models import Tlp

THEHIVE_URL = 'http://127.0.0.1:9000'
THEHIVE_API_KEY = '**YOUR_API_KEY**'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

# Create a new domain artifact
artifact = AlertArtifact(dataType='domain', data='malicious-domain.tld', ignoreSimilarity=True, ioc=True)
response = api.create_alert_artifact(ALERT_ID, artifact)

# Update its tlp, sighted and ignoreSimilarity flags
artifact_data = response.json()[0]
artifact_data['tlp'] = Tlp.RED.value
artifact_data['sighted'] = True
artifact_data['ignoreSimilarity'] = False

new_artifact = AlertArtifact(json=artifact_data)
api.update_alert_artifact(artifact_data['id'], new_artifact, fields=['tlp', 'ioc', 'ignoreSimilarity'])
```

## Delete an Alert Artifact

Delete an existing alert artifact identified by `ARTIFACT_ID`

!!! Warning
    This function is available in TheHive 4 ONLY
    
```python
from thehive4py.api import TheHiveApi

THEHIVE_URL = 'http://127.0.0.1:9000'
THEHIVE_API_KEY = '**YOUR_API_KEY**'

api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

# Delete alert artifact
api.delete_alert_artifact(ARTIFACT_ID)
```