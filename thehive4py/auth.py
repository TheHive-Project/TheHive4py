#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests.auth import AuthBase


class BasicAuth(AuthBase):
    """
    A custom basic authentication class for requests, that takes into account the organisation header
    """
    def __init__(self, username, password, organisation=None):
        """
        Constructor

        Arguments:
            username (str): The username to use for the authentication.
            password (str): The password to use for the authentication.
            organisation (str): The organisation to use.
        """
        self.username = username
        self.password = password
        self.organisation = organisation

    def __call__(self, req):
        req.headers['Authorization'] = requests.auth._basic_auth_str(self.username, self.password)

        if self.organisation is not None:
            req.headers['X-Organisation'] = self.organisation

        return req


class BearerAuth(AuthBase):
    """
    A custom authentication class for requests, relying on API key (Bearer authorization header), 
    and taking into account the organisation header
    """
    def __init__(self, api_key, organisation=None):
        """
        Constructor

        Arguments:
            api_key (str): The API Key to use for the authentication
            organisation (str): The organisation to use.
        """    
        self.api_key = api_key
        self.organisation = organisation

    def __call__(self, req):
        req.headers['Authorization'] = 'Bearer {}'.format(self.api_key)

        if self.organisation is not None:
            req.headers['X-Organisation'] = self.organisation

        return req
