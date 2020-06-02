
## Create a file observable

```python
import sys
import json
from thehive4py.api import TheHiveApi
from thehive4py.models import CaseObservable

# Init the CaseObserablae object
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

# Init the CaseObserablae object
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

!!! missing
    TODO

## Search ip observables of a given case

!!! missing
    TODO