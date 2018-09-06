from typing import List

from .abstract import AbstractController
from ..models import User


class UsersController(AbstractController):
    def __init__(self, api):
        AbstractController.__init__(self, 'user', api)

    def find_all(self, query, **kwargs) -> List[User]:
        return self._wrap(self._find_all(query, **kwargs), User)

    def find_one_by(self, query, **kwargs) -> User:
        return self._wrap(self._find_one_by(query, **kwargs), User)

    def get_by_id(self, org_id) -> User:
        return self._wrap(self._get_by_id(org_id), User)

    def create(self, data) -> User:

        if isinstance(data, dict):
            data = User(data).json()
        elif isinstance(data, User):
            data = data.json()

        response = self._api.do_post('user', data).json()

        return User(response)

    def update(self, user_id, data, fields=None) -> User:
        url = 'user/{}'.format(user_id)
        patch = AbstractController._clean_changes(data, ['name', 'roles'], fields)
        return self._wrap(self._api.do_patch(url, patch).json(), User)

    def lock(self, user_id) -> User:
        user = self._api.do_patch('user/{}'.format(user_id), {
            'status': 'Locked'
        }).json()

        return User(user)

    def set_password(self, user_id, password):
        self._api.do_post('user/{}/password/set'.format(user_id), {'password': password})

        return True

    def change_password(self, user_id, current_password, new_password ):
        self._api.do_post('user/{}/password/change'.format(user_id), {
            'currentPassword': current_password,
            'password': new_password
        })

        return True

    def set_key(self, user_id):
        return self._api.do_post('user/{}/key/renew'.format(user_id), {}).text

    def renew_key(self, user_id):
        return self.set_key(user_id)

    def get_key(self, user_id):
        return self._api.do_get('user/{}/key'.format(user_id)).text

    def revoke_key(self, user_id):
        return self._api.do_delete('user/{}/key'.format(user_id))