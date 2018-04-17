## Initialize an api client

```
from thehive4py.api import Api

api = Api('http://localhost:9000', '**API_KEY**')
```

## Cases methods

```python
api.cases.find_all(query, sort='', range='')
api.cases.find_one_by(query, sort='')
api.cases.count(query)
api.cases.get_by_id(id)
api.cases.get_by_number(number)
api.cases.get_tasks(case_id, query, sort='', range='')
api.cases.get_observables(case_id, query, sort='', range='')
api.cases.links(case_id)
api.cases.has_observable(case_query, observable_query)
```

## Observables methods

``` python
api.observables.find_all(query, sort='', range='')
api.observables.find_one_by(query, sort='')
api.observables.count(query)
api.observables.get_by_id(id)
api.observables.of_case(case_id, query, sort='', range='')
```

## Tasks methods

```python
api.tasks.find_all(query, sort='', range='')
api.tasks.find_one_by(query, sort='')
api.tasks.count(query)
api.tasks.get_by_id(id)
api.tasks.of_case(case_id, query, sort='', range='')
```

## Alerts methods

```python
api.alerts.find_all(query, sort='', range='')
api.alerts.find_one_by(query, sort='')
api.alerts.count(query)
api.alerts.get_by_id(id)
```