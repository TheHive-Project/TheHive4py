import json
import uuid
import time
from thehive4py.api import Api
from thehive4py.models import Metric
from thehive4py.query import *


def log(title, result):
    print('------- {} --------'.format(title))
    if isinstance(result, dict) or isinstance(result, list):
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(result)


api = Api('http://localhost:9000', 'tBhBXMvsVJYrwcc6Qj9G9OE91m5a/PeF', proxies={
    'http': 'http://localhost:8080',
    'https': 'http://localhost:8080'
})

# Fetch alerts
metrics = api.metrics.find_all()
log('Metrics', list(map(lambda i: i.json(), metrics)))

log('Metric by id', api.metrics.get_by_id(metrics[0].id))

field_name = str(uuid.uuid4())[0:6]

metric = api.metrics.create({
    'name': field_name,
    'description': field_name,
    'title': field_name
})
log('New Metric', metric)
log('New Metric by id', api.metrics.get_by_id(metric.id))
log('Delete it', api.metrics.remove(metric.id))
