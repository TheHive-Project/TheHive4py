import json
import uuid
import time
from thehive4py.api import Api
from thehive4py.models import CustomField
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
custom_fields = api.customfields.find_all()
log('Custom fields', list(map(lambda i: i.json(), custom_fields)))

log('Custom fields by id', api.customfields.get_by_id(custom_fields[0].id))

field_name = str(uuid.uuid4())[0:6]

custom_field = api.customfields.create({
    'name': field_name,
    'description': field_name,
    'reference': field_name,
    'type': 'string'
})
log('New Custom field', custom_field)
log('New Custom field by id', api.customfields.get_by_id(custom_field.id))
log('Delete it', api.customfields.remove(custom_field.id))
