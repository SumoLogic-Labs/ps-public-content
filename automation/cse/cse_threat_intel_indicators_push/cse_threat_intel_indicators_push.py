#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Julien Bernard'
# __email = 'julien@sumologic.com'
# __description__ = 'A management script to push CSE Threat Intel Source Indicators'

'''
Input CSV file must be in the folllowing format (with headers):

value,description,expiration
www.google.xxx,bad domain,
10.10.10.10,bad IP,2023-07-05T17:04:50Z
user@domain.com,bad user,
'''

# modules import
import argparse
from ftplib import all_errors
import json
import sys
import urllib3
import csv


# main script
if __name__ == '__main__':
    # command line variables handling
    parser = argparse.ArgumentParser(description='A management script to push CSE Threat Intel Source Indicators')

    # required arguments
    required = parser.add_argument_group('required arguments')
    required.add_argument('-accessid', type=str, nargs=1, help='Sumo Logic API Access ID', required=True)
    required.add_argument('-accesskey',type=str, nargs=1, help='Sumo Logic API Access KEY', required=True)
    required.add_argument('-threatIntelSourceId', type=str, nargs=1, help='CSE Threat Intel Source ID', required=True)
    required.add_argument('-input', type=str, nargs=1, help='Input CSV file', required=True)

    # optional arguments
    parser.add_argument('-env', type=str, nargs=1, help='Sumo Logic Environment (default: "us2")')
 
    args = parser.parse_args()

    # Sumo Logic API Access configuration
    SUMO_API_ACCESS_ID = args.accessid[0]
    SUMO_API_ACCESS_KEY = args.accesskey[0]

    # Sumo Logic instance environment
    if args.env:
        SUMO_API_URL =  "https://api.{}.sumologic.com/api/".format(args.env[0])
    else:
        SUMO_API_URL =  "https://api.us2.sumologic.com/api/"

    # API authentication and headersconfiguration
    auth= "{}:{}".format(SUMO_API_ACCESS_ID, SUMO_API_ACCESS_KEY)
    headers = urllib3.make_headers(basic_auth=auth)
    headers.setdefault('Content-Type', 'application/json')
    headers.setdefault('Accept', 'application/json')
    http = urllib3.PoolManager()

    # Loading CSV file content
    input_file = csv.DictReader(open(args.input[0]))
    for row in input_file:
        ioc_value = str(row["value"])
        ioc_description = str(row["description"])
        ioc_expiration = str(row["expiration"])

        print("Adding IOC: {:30s} | {:40s} | {}".format(ioc_value, ioc_description,ioc_expiration))

        if ioc_expiration == "":
             data = {"indicators":[{"active":True, "description": ioc_description, "value": ioc_value}]}
        else:
             data = {"indicators":[{"active":True, "description": ioc_description, "expiration": ioc_expiration, "value": ioc_value}]}

        encoded_data =json.dumps(data).encode('utf-8')

        request = http.request('POST', "{}sec/v1/threat-intel-sources/{}/items".format(SUMO_API_URL, args.threatIntelSourceId[0]), headers=headers, body=encoded_data)
        request_status = request.status

        if request_status != 200:
            print("Request not accepted. Response code: {}".format(request_status))
        else:
            print("\t- OK")