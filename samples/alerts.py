import json
import uuid
import time
from thehive4py.api import Api
from thehive4py.models import Alert, AlertArtifact, CustomFieldHelper
from thehive4py.query import *


def log(title, result):
    print('------- {} --------'.format(title))
    if isinstance(result, dict) or isinstance(result, list):
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(result)


api = Api('http://localhost:9000', 'tBhBXMvsVJYrwcc6Qj9G9OE91m5a/PeF', proxies={
    #'http': 'http://localhost:8080',
    #'https': 'http://localhost:8080'
})

# Fetch alerts
some_alerts = api.alerts.find_all(And({'status': 'New'}, {'type': 'external'}), range='0-2')
log('New Alerts', list(map(lambda i: i.json(), some_alerts)))

# Prepare the custom fields
customFields = CustomFieldHelper()\
    .add_boolean('booleanField', True)\
    .add_string('businessImpact', 'HIGH')\
    .add_date('occurDate', int(time.time())*1000)\
    .add_number('cvss', 9)\
    .build()

sourceRef = str(uuid.uuid4())[0:6]

ip_artifact = AlertArtifact({'dataType': 'ip', 'data': '8.8.8.8'})
file_artifact = AlertArtifact({'dataType': 'file', 'data': './observable.file.txt'})
mail_artifact = AlertArtifact({
    'dataType': 'mail',
    'data': '{}@sample.com'.format(str(uuid.uuid4())[0:10])
})

new_alert = api.alerts.create(Alert({
    'title': 'New Alert from TH4P 2.0',
    'tlp': 2,
    'tags': ['TheHive4Py', 'sample'],
    'description': 'N/A',
    'type': 'external',
    'source': 'thehive4py',
    'sourceRef': sourceRef,
    'artifacts': list(map(lambda a: a.json(), [ip_artifact, file_artifact, mail_artifact])),
    'customFields': customFields
}))
log('New alert with', new_alert.json())

api.alerts.update(new_alert.id, {'tlp': 1}, fields=['tlp'])

api.alerts.mark_as_read(new_alert.id)
api.alerts.mark_as_unread(new_alert.id)
api.alerts.follow(new_alert.id)
api.alerts.unfollow(new_alert.id)
# api.alerts.import_as_case(new_alert.id, 'IOC')
# api.alerts.merge_into(new_alert.id, 'CASE_ID')
