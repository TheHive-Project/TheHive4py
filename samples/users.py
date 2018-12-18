import json
import uuid

from thehive4py.api import Api
from thehive4py.models import User
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

log('Some users', list(map(lambda i: i.json(), api.users.find_all(Eq('status', 'Ok'), range='0-2'))))

# Create organization
rand = str(uuid.uuid4())[:6]
new_user = api.users.create(User({
    'login': 'User-{}'.format(rand),
    'name': 'User {}'.format(rand),
    'roles': ['read', 'write'],
    'status': 'Ok'
}))
log('new user', new_user.json())
log('new user update', api.users.update(new_user.id, new_user.json(), ['name', 'roles']))
log('new user update', api.users.update(new_user.id, {
    "name": "{} UPDATED".format(new_user.name)
}, ['name']))

user_id = new_user.id

log('set password', api.users.set_password(user_id, 'password'))
# log('change password', api_sa.users.change_password(user_id, 'password', 'password2'))
# log('set key', api.users.set_key(user_id))
# log('get key', api.users.get_key(user_id))
# log('renew key', api.users.renew_key(user_id))
# log('get key', api.users.get_key(user_id))
# log('revoke key', api.users.revoke_key(user_id))
# log('lock new user', api.users.lock(user_id))
