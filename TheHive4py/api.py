#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json
import os
import re



class theHive():


    """
        Python API for TheHive

        :param url: thehive URL
        :param username: username
        :param password: password

    """

    def __init__(self, url, username, password):

        self.url = url
        self.username = username
        self.password = password
        try:
            import requests
            self.session = requests.Session()
            self.auth = requests.auth.HTTPBasicAuth(username=self.username,
                                                    password=self.password)
        except Exception as excp:
            return "requests library is non installed"



    def get_case(self, caseId):
        path = "/api/case/"+caseId
        req = self.url+path
        return self.session.get(req, auth=self.auth)

    def get_case_observables(self, caseId):
        path = "/api/case/artifact/_search"
        req = self.url+ path
        data = {
                "query": {
                    "_and": [{
                        "_parent": {
                            "_type": "case",
                            "_query": {
                                "_id": caseId
                            }
                        }
                    }, {
                        "status": "Ok"
                    }]
                }
            }

        return self.session.post(req, json=data, auth=self.auth)
