#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Julien Bernard'
# __email = 'julien@sumologic.com'
# __description__ = 'A management script to update CSE entities for travelling users.'

'''
Prerequesists:
    - Create a new CSE Match list:
        - Name: "travelling_users"
        - Description: Users currently travelling. This match list is used to disable some rules (impossible travel, first seen country, etc.) via tuning rule "Travelling Users". When adding a new user, set the auto-expiration date.
        - TTL: none
        - Target column: Username   

    - Create a new CSE Tuning Rule:
        - Name: "Travelling Users"
        - Rules:
            - THRESHOLD-S00097: Impossible Travel - Successful
            - THRESHOLD-S00098: Impossible Travel - Unsuccessful
            - FIRST-S00029: First Seen Successful Authentication From Unexpected Country
        - Type: EXCLUDE
        - Expression: 
            array_contains(listMatches, 'travelling_users')

    - Create a new CSE Entity Criticality:
        - Name: "Travelling Users"
        - Expression: severity + 2

    - Add travelling users into the "travelling_users" match list.
        - Add an expiration date, so the user will be automatically removed from the list

    - Update the script with:
        - CSE_TRAVELLING_USERS_MATCHLIST_ID
        - CSE_TRAVELLING_USERS_TAG 
        - CSE_TRAVELLING_USERS_CRITICALITY
        - SUMO_API_ACCESS_ID
        - SUMO_API_ACCESS_KEY

    - Schedule the execution of that script at least once a day to synchornize (add/remove) the tag and criticality on entities.

Limitations:
    - It can take a few seconds before the changes applied using API get refelected in CSE UI

'''


# modules import
import json
import urllib3

# CSE "travelling_users" resources
CSE_TRAVELLING_USERS_MATCHLIST_ID = 182
CSE_TRAVELLING_USERS_TAG = "Travelling User"
CSE_TRAVELLING_USERS_CRITICALITY = "Travelling Users"


# Sumo Logic API Access configuration
SUMO_API_URL =  "https://api.us2.sumologic.com/api/"
SUMO_API_ACCESS_ID = "XXX"
SUMO_API_ACCESS_KEY = "XXX"


# API authentication and headersconfiguration
auth= "{}:{}".format(SUMO_API_ACCESS_ID, SUMO_API_ACCESS_KEY)
headers = urllib3.make_headers(basic_auth=auth)
headers.setdefault('Content-Type', 'application/json')
headers.setdefault('Accept', 'application/json')
http = urllib3.PoolManager()


# Function: get the list of users in the match list
def get_users_in_matchlist():
    print("- Getting the list of users in matchlist: {}".format(CSE_TRAVELLING_USERS_MATCHLIST_ID))

    request = http.request('GET', "{}sec/v1/match-list-items?listIds={}&limit=1000".format(SUMO_API_URL, CSE_TRAVELLING_USERS_MATCHLIST_ID), headers=headers)
    request_status = request.status

    output = []
    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        exit()
    else:
        jsonObject = json.loads(request.data.decode("utf-8"))
        users = jsonObject['data']['objects']

        for user in users:
            user_name = user['value']
            print("\t- Found user: {}".format(user_name))
            output.append(user_name)

    return output


# Function: get the list of users already tagged
def get_users_with_tag():
    print("- Getting the list of user entities with tag: {}".format(CSE_TRAVELLING_USERS_TAG))

    request = http.request('GET', "{}sec/v1/entities?q=tag:\"{}\"&limit=100".format(SUMO_API_URL, CSE_TRAVELLING_USERS_TAG), headers=headers)
    request_status = request.status

    output = []
    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        exit()
    else:
        jsonObject = json.loads(request.data.decode("utf-8"))
        users = jsonObject['data']['objects']

        for user in users:
            user_name = user['value']
            print("\t- Found user: {}".format(user_name))
            output.append(user_name)

    return output


# Function: get the list of users having the criticality applied
def get_users_with_criticality():
    print("- Getting the list of user entities with criticality: {}".format(CSE_TRAVELLING_USERS_CRITICALITY))

    request = http.request('GET', "{}sec/v1/entities?q=criticality:\"{}\"&limit=100".format(SUMO_API_URL, CSE_TRAVELLING_USERS_CRITICALITY), headers=headers)
    request_status = request.status

    output = []
    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        exit()
    else:
        jsonObject = json.loads(request.data.decode("utf-8"))
        users = jsonObject['data']['objects']

        for user in users:
            user_name = user['value']
            print("\t- Found user: {}".format(user_name))
            output.append(user_name)

    return output


# Function: add tag to an existing user entity
def entity_add_tag(user, tag):
    entity_id = "_username-{}".format(user)

    data = {"tags":[tag]}
    encoded_data =json.dumps(data).encode('utf-8')
    
    request = http.request('POST', "{}sec/v1/entities/{}/tags".format(SUMO_API_URL, entity_id), headers=headers, body=encoded_data)
    request_status = request.status

    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        exit()
    else:
        jsonObject = json.loads(request.data.decode("utf-8"))
        print("\t\t\t- Done!")


# Function: remove tag from an entity
def entity_remove_tag(user, tag):
    entity_id = "_username-{}".format(user)

    data = {"tags":[tag]}
    encoded_data =json.dumps(data).encode('utf-8')
    
    request = http.request('DELETE', "{}sec/v1/entities/{}/tags".format(SUMO_API_URL, entity_id), headers=headers, body=encoded_data)
    request_status = request.status

    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        exit()
    else:
        jsonObject = json.loads(request.data.decode("utf-8"))
        print("\t\t\t- Done!")


# Function: add criticality to an existing user entity
def entity_add_criticality(user, criticality):
    entity_id = "_username-{}".format(user)

    data = {"criticality": criticality}
    encoded_data =json.dumps(data).encode('utf-8')
    
    request = http.request('PUT', "{}sec/v1/entities/{}/criticality".format(SUMO_API_URL, entity_id), headers=headers, body=encoded_data)
    request_status = request.status

    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        exit()
    else:
        jsonObject = json.loads(request.data.decode("utf-8"))
        print("\t\t\t- Done!")


# Function: remove criticality to an existing user entity
def entity_remove_criticality(user):
    entity_id = "_username-{}".format(user)

    data = {"criticality": ""}
    encoded_data =json.dumps(data).encode('utf-8')
    
    request = http.request('PUT', "{}sec/v1/entities/{}/criticality".format(SUMO_API_URL, entity_id), headers=headers, body=encoded_data)
    request_status = request.status

    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        exit()
    else:
        jsonObject = json.loads(request.data.decode("utf-8"))
        print("\t\t\t- Done!")


# main script
if __name__ == '__main__':
    # list users
    users_in_matchlist = get_users_in_matchlist()
    users_with_tag = get_users_with_tag()
    users_with_criticality = get_users_with_criticality()

    # Process users
    print("- Reviewing users")

    # Users listed in the match list
    for user in users_in_matchlist:
        print("\t- User {} is in the match list".format(user))
        if user in users_with_tag:
            print("\t\t- User {} is already tagged - nothing to do".format(user))
        else:
            print("\t\t- User {} is not tagged - adding tag now".format(user))
            entity_add_tag(user, CSE_TRAVELLING_USERS_TAG)

        if user in users_with_criticality:
            print("\t\t- User {} already has the criticality applied - nothing to do".format(user))
        else:
            print("\t\t- User {} has not the criticality applied - adding criticality now".format(user))
            entity_add_criticality(user, CSE_TRAVELLING_USERS_CRITICALITY)
    
    # Users having the tag applied
    for user in users_with_tag:
        print("\t- User {} has tag applied".format(user))
        if user in users_in_matchlist:
            print("\t\t- User {} is still in the match list - nothing to do".format(user))
        else:
            print("\t\t- User {} is not in the match list anymore - removing tag now".format(user))
            entity_remove_tag(user, CSE_TRAVELLING_USERS_TAG)

    # Users having the criticality applied
    for user in users_with_criticality:
        print("\t- User {} has criticality applied".format(user))
        if user in users_in_matchlist:
            print("\t\t- User {} is still in the match list - nothing to do".format(user))
        else:
            print("\t\t- User {} is not in the match list anymore - removing criticality now".format(user))
            entity_remove_criticality(user)

    print("- All done!")
    exit(0)
