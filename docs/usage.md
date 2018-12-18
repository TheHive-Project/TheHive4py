## Initialize an api client

```python
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

api.cases.get_tasks(case_id, query, **kwargs)        
api.cases.get_observables(case_id, query, **kwargs)
api.cases.add_task(case_id, task)
api.cases.add_observable(case_id, observable)

api.cases.run_responder(cortex_id, case_id, responder_name)

api.cases.stats_by(query, field, top=10)

```

## Observables methods

```python
api.observables.find_all(query, sort='', range='')
api.observables.find_one_by(query, sort='')
api.observables.count(query)
api.observables.get_by_id(id)
api.observables.of_case(case_id, query, sort='', range='')

api.observables.of_type(data_type, query={}, **kwargs)
api.observables.create(case_id, data)      
api.observables.update(observable_id, data, fields=None)
        
api.observables.run_analyzer(cortex_id, observable_id, analyzer_id)
api.observables.run_responder(cortex_id, observable_id, responder_name)

api.observables.stats_by(query, field, top=10)

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
api.tasks.remove(query)

api.tasks.run_responder(cortex_id, task_id, responder_name)
api.tasks.stats_by(query, field, top=10)

```

## Task logs methods

```python
api.tasklogs.find_all(task_id, query, sort='', range='')
api.tasklogs.find_one_by(query, sort='')
api.tasklogs.count(query)
api.tasklogs.get_by_id(task_log_id)
api.tasklogs.of_task(task_id)
api.tasklogs.create(data)
api.tasklogs.remove(task_log_id)
api.tasklogs.run_responder(cortex_id, alert_id, responder_name)
```

## Alerts methods

```python
api.alerts.find_all(query, sort='', range='')
api.alerts.find_one_by(query, sort='')
api.alerts.count(query)
api.alerts.get_by_id(id)
api.alert.mark_as_read(id)
api.alert.mark_as_unread(id)
api.alert.follow(id)
api.alert.unfollow(id)

api.alerts.import_as_case(alert_id, template=None)
api.alerts.merge_into(alert_id, case_id)
api.alerts.run_responder(cortex_id, alert_id, responder_name)

api.alerts.stats_by(query, field, top=10)
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

## Metrics methods

```python
api.metrics.find_all()
api.metrics.get_by_id(id)
api.metrics.create(data)
api.metrics.remove(id)
```

## Custom fields methods

```python
api.customfields.find_all()
api.customfields.get_by_id(id)
api.customfields.create(data)
api.customfields.remove(id)
```