# Code samples for observable operations

## Create a file observable

```python
import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')

# Init the CaseObservable object
file_observable = CaseObservable(dataType='file',
    data=['pic.png'],
    tlp=1,
    ioc=True,
    sighted=True,
    tags=['thehive4py'],
    message='test'
)

# Call the API
response = api.create_case_observable(CASE_ID, file_observable)

# Display the result
if response.status_code == 201:
    # Get response data
    observableJson = response.json()

    # Display response data
    print(json.dumps(observableJson, indent=4, sort_keys=True))
else:
    print('Failure: {}/{}'.format(response.status_code, response.text))

sys.exit(0)
```

## Create a domain observable

```python
import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')

# Init the CaseObservable object
domain = CaseObservable(dataType='filename',
    data=['pic.png'],
    tlp=1,
    ioc=True,
    sighted=True,
    tags=['thehive4py'],
    message='test'
)

# Call the API
response = api.create_case_observable(CASE_ID, domain)

# Display the result
if response.status_code == 201:
    # Get response data
    observableJson = response.json()

    # Display response data
    print(json.dumps(observableJson, indent=4, sort_keys=True))
else:
    print('Failure: {}/{}'.format(response.status_code, response.text))

sys.exit(0)
```

## Get all observables of a given case

```python
import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')

# Call the API
response = api.get_case_observables(CASE_ID, query={}, sort=['-startDate', '+ioc'], range='all')

# Display the result
if response.status_code == 200:
    # Get response data
    list = response.json()

    # Display response data
    print(json.dumps(list, indent=4, sort_keys=True))
else:
    print('Failure: {}/{}'.format(response.status_code, response.text))

sys.exit(0)
```

## Search ip observables of a given case

```python
import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable
from thehive4py.query import Eq, And

api = TheHiveApi('http://127.0.0.1:9000', '**YOUR_API_KEY**')

# Build query
query = And(Eq('dataType', 'ip'), Eq('ioc', True))

# Call the API to search all case's ip observables marked as IOC, sort them by descending startDate
response = api.get_case_observables(CASE_ID, query=query, sort=['-startDate'], range='all')

# Display the result
if response.status_code == 200:
    # Get response data
    list = response.json()

    # Display response data
    print(json.dumps(list, indent=4, sort_keys=True))
else:
    print('Failure: {}/{}'.format(response.status_code, response.text))

sys.exit(0)
```