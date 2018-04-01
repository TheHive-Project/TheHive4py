import requests
import sys
import warnings


class TheHive4py(object):
    """This is the main class for communicating with the TheHive API. As this is a new major version, authentication is
    only possible through the api key. Basic auth with user/pass is deprecated."""
    def __init__(self, url, api_key, **kwargs):
        if not isinstance(url, type(str)) or not isinstance(api_key, type(str)):
            raise TypeError('URL and API key are required and must be of type string.')

        # Drop a warning for python2 because reasons
        if sys.version[0] < 3:
            warnings.warn('You are using Python 2.x. That can work, but is not supported.')

        # Create new session object with an Authorization header
        self.__session = requests.Session()
        self.__session.headers.update({
            'Authorization': 'Bearer {}'.format(api_key)
        })
        self.__url = url
        self.__endpoint = '{}/api/'.format(url)

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
