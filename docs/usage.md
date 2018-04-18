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

api.cases.flag(flag)
api.cases.close(case_id)
api.cases.open(case_id)

api.cases.add_metric(case_id, metric, value)
api.cases.remove_metric(case_id, metric)
api.cases.add_customfield(case_id, customfield, value)
api.cases.remove_customfield(case_id, customfield, value)
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

api.tasks.get_waiting(query, sort='', range='')
api.tasks.get_by_user(user_id, query, sort='', range='')
api.tasks.get_logs(query, sort='', range='')
api.tasks.add_log(task_log)

api.tasks.flag(query, flag)
api.tasks.close(query)
api.tasks.open(query)
api.tasks.cancel(query)
```

## Alerts methods

```python
api.alerts.find_all(query, sort='', range='')
api.alerts.find_one_by(query, sort='')
api.alerts.count(query)
api.alerts.get_by_id(id)

api.alerts.import_as_case(alert_id, template=None)
api.alerts.merge_into(alert_id, case_id)
```

## Users methods

```python
api.users.find_all(query, sort='', range='')
api.users.find_one_by(query, sort='')
api.users.count(query)
api.users.get_by_id(id)

api.users.lock(id)
api.users.unlock(id)
api.users.get_key(id)
api.users.create_key(id)
api.users.revoke_key(id)
```