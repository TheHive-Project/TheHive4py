import requests
import sys
import json
import warnings

from .exceptions import *
from .controller.cases import CasesController
from .controller.tasks import TasksController
from .controller.observables import ObservablesController
from .controller.alerts import AlertsController
from .controller.users import UsersController


class Api(object):
    """This is the main class for communicating with the TheHive API. As this is a new major version, authentication is
    only possible through the api key. Basic auth with user/pass is deprecated."""
    def __init__(self, url, api_key, **kwargs):
        if not isinstance(url, str) or not isinstance(api_key, str):
            raise TypeError('URL and API key are required and must be of type string.')

        # Drop a warning for python2 because reasons
        if int(sys.version[0]) < 3:
            warnings.warn('You are using Python 2.x. That can work, but is not supported.')

        self.__api_key = api_key
        self.__url = url
        self.__base_url = '{}/api/'.format(url)
        self.__proxies = kwargs.get('proxies', {})
        self.__verify_cert = kwargs.get('verify_cert', kwargs.get('cert', True))

        self.cases = CasesController(self)
        self.tasks = TasksController(self)
        self.observables = ObservablesController(self)
        self.alerts = AlertsController(self)
        self.users = UsersController(self)

    @staticmethod
    def __recover(exception):

        if isinstance(exception, requests.exceptions.HTTPError):
            if exception.response.status_code == 404:
                raise NotFoundError("Resource not found") from exception
            elif exception.response.status_code == 401:
                raise AuthenticationError("Authentication error") from exception
            elif exception.response.status_code == 403:
                raise AuthorizationError("Authorization error") from exception
            else:
                raise InvalidInputError("Invalid input exception") from exception
        elif isinstance(exception, requests.exceptions.ConnectionError):
            raise ServiceUnavailableError("Cortex service is unavailable") from exception
        elif isinstance(exception, requests.exceptions.RequestException):
            raise ServerError("Cortex request exception") from exception
        else:
            raise TheHiveError("Unexpected exception") from exception

    def do_get(self, endpoint, params={}):
        headers = {
            'Authorization': 'Bearer {}'.format(self.__api_key)
        }

        try:
            response = requests.get('{}{}'.format(self.__base_url, endpoint),
                                    headers=headers,
                                    params=params,
                                    proxies=self.__proxies,
                                    verify=self.__verify_cert)

            response.raise_for_status()
            return response
        except Exception as ex:
            self.__recover(ex)

    def do_file_post(self, endpoint, data, **kwargs):
        headers = {
            'Authorization': 'Bearer {}'.format(self.__api_key)
        }

        try:
            response = requests.post('{}{}'.format(self.__base_url, endpoint),
                                     headers=headers,
                                     proxies=self.__proxies,
                                     data=data,
                                     verify=self.__verify_cert,
                                     **kwargs)
            response.raise_for_status()
            return response
        except Exception as ex:
            self.__recover(ex)

    def do_post(self, endpoint, data, params={}, **kwargs):
        headers = {
            'Authorization': 'Bearer {}'.format(self.__api_key),
            'Content-Type': 'application/json'
        }

        try:
            response = requests.post('{}{}'.format(self.__base_url, endpoint),
                                     headers=headers,
                                     proxies=self.__proxies,
                                     json=data,
                                     params=params,
                                     verify=self.__verify_cert,
                                     **kwargs)
            response.raise_for_status()
            return response
        except Exception as ex:
            self.__recover(ex)

    def do_patch(self, endpoint, data, params={}):
        headers = {
            'Authorization': 'Bearer {}'.format(self.__api_key),
            'Content-Type': 'application/json'
        }

        try:
            response = requests.patch('{}{}'.format(self.__base_url, endpoint),
                                      headers=headers,
                                      proxies=self.__proxies,
                                      json=data,
                                      params=params,
                                      verify=self.__verify_cert)
            response.raise_for_status()
            return response
        except Exception as ex:
            self.__recover(ex)

    def do_delete(self, endpoint):
        headers = {
            'Authorization': 'Bearer {}'.format(self.__api_key)
        }

        try:
            response = requests.delete('{}{}'.format(self.__base_url, endpoint),
                                       headers=headers,
                                       proxies=self.__proxies,
                                       verify=self.__verify_cert)
            response.raise_for_status()
            return True
        except Exception as ex:
            self.__recover(ex)
        pass

    def status(self):
        return self.do_get('status')

    # Handling cases
    def case_create(self, **kwargs):
        """Creates a new case in TheHive."""
        pass

    def case_update(self):
        """Updates given attributes of a case. This function is also used for closing cases. Maybe a wrapper for that
        would be cool, too."""
        pass

    # Handling observables
    def observable_create(self):
        """
        Creates a new observable attached to a case.
        Necessary for creating a new observable is
        - the case number or the case id (speaking of elasticsearch document id)
        - the data type of the observable to add
        - the value itself
        """
        pass

    def observable_update(self):
        """Updates an observable based on the observable id. Not sure if this is relevant though."""
        pass

    def observable_remove(self):
        """Removes an observable based on the observable id."""
        pass

    # Handling tasks
    def task_create(self):
        """Creates a new task attached to a case. Necessary for the creation is
        - the case number or the case id
        - the task name
        - the task description."""
        pass

    def task_update(self):
        pass

    def task_remove(self):
        pass

    # Administration
    def user_add(self):
        pass

    def user_deactivate(self):
        pass
