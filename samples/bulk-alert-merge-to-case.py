#!/usr/bin/env python3 -tt
# -*- coding: utf-8 -*-

# This is documented a little more heavily then typical to help others fully understand what's being
# done at each step and why it was done so that it can be easily repurposed. 

import sys
import json
import time
import requests
from thehive4py.api import TheHiveApi
from thehive4py.query import Eq, String
from tqdm import tqdm # Optional package - this will just give you a status bar of how much time is left


def main():
    api_key = '**YOUR_API_KEY**'
    hive_url = 'http://127.0.0.1:9000'
    api = TheHiveApi(hive_url, api_key)
    alert_title = input('[*] What is the title of the alert you want to merge?: ')
    case_num = input('[*] What is the case number you want to merge the alert(s) into?: ')
    
    # New alerts start at 0, so if a new alert just came in it'd be 0, where an 
    # alert that arrived last week may be number 100
    total_alerts = input('[*] How many alerts back do you want to query?: ')

    alert_id = [] # This is the list of alert id(s) to be merged into the case

    try:
        def search_cases(query, range, sort):
            """
            This function returns the case id for the case number specified by user
            or prints an error if it's unable to connect to Hive for the query.
            
            If a the HTTP Status code is 200, it returns the case data in question as a JSON.
            """
            # Query being what am I looking for, range being how far back to go
            # Sort I *THINK* defines how you want them returned
            case_response = api.find_cases(query=query, range=range, sort=sort)

            if case_response.status_code == 200:
                return case_response.json()
            else:
                print('[*] Invalid HTTP Response. Response != 200')
                sys.exit(0)
        
        # Performing the above function - attempts to find the case number specified at the start
        case_prep = search_cases(Eq('caseId', case_num), 'all', [])
        # Since they are returned as a list, we choose the first item in the list and specifically the
        # case '_id' field - this field is not visible through the gui but is needed later.
        case_id = case_prep[0]['_id']
    except Exception as e:
        print(e)
        print('[*] Failed to retrieve Case ID')
        sys.exit(0)
    
    try:
        # Query being what am I looking for, range being how far back to go
        # Sort I *THINK* defines how you want them returned
        def search_alerts(query, range, sort):
            response = api.find_alerts(query=query, range=range, sort=sort)

            if response.status_code == 200:
                return response.json()
            else:
                print('[*] Invalid HTTP Response. Response != 200')
                sys.exit(0)
        
        # Adds all alerts with a title that matches the input specified, searches through alerts
        # as far back as specified, and returns a list of alerts in JSON format
        all_alert_info = search_alerts(String("title:'%s'" % (alert_title)), '0-' + str(total_alerts), [])
    except Exception as e:
        print(e)
        print('[*] Failed to connect/retrieve alerts')
        sys.exit(0)

    try:
        for alert in all_alert_info:
            if alert['status'] == 'New': # This validates that we're only attempting to merge New alerts that haven't been imported/read
                # Below ensures only the alerts with the same title are merged.
                if alert['title'].lower().strip() == alert_title.lower().strip(): # *IMPORTANT* If this isn't done partial matches will be added
                    alert_id.append(alert['id']) # the alert 'id' field to the alert_id list. This field is not visible in the gui
    except Exception as e:
        print(e)
        print('[*] Failed to append alerts to list')
        sys.exit(0)

    try:
        for alerts in tqdm(alert_id): # tqdm is option - only adds a progress bar, remove tqdm() and it will work without it
            headers = {'Authorization': 'Bearer ' + api_key} # provides header data needed for script to auth with Hive
            # Below sends the post request that does the actual merge. It uses the hidden alert/case id fields.
            # DO NOT add a / after the last %s or it will not work
            requests.post(hive_url + '/api/alert/%s/merge/%s' % (alerts, case_id), headers=headers) 
            time.sleep(.1) # To prevent merge errors from being sent to quickly.
        print('[*] Merge Complete.')
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
