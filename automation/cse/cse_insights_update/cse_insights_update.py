#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ = 'Julien Bernard'
# __email = 'julien@sumologic.com'
# __description__ = 'A management script for listing and updating CSE Insights'

# modules import
import argparse
import json
import sys
import urllib3

# get insights
def get_insights(insights_filter, http_headers, insights_offset):   
    http = urllib3.PoolManager()
    request = http.request('GET', "{}sec/v1/insights?q={}&offset={}".format(SUMO_API_URL, insights_filter, insights_offset), headers=http_headers)
    request_status = request.status

    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        sys.exit()

    payload = json.loads(request.data.decode('utf-8'))
    current_insights = payload['data']['objects']
    more_insights = payload['data']['hasNextPage']

    return(current_insights, more_insights)

# tag insight
def insight_add_tag(id, http_headers, tag):
    data = {"tagName": tag}

    http = urllib3.PoolManager()
    encoded_data =json.dumps(data).encode('utf-8')

    request = http.request('POST', "{}sec/v1/insights/{}/tags".format(SUMO_API_URL, id), headers=http_headers, body=encoded_data)
    request_status = request.status

    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status)) 
        exit()
    else:
        print("\t- Tag added.")

# comment insight
def insight_add_comment(id, http_headers, comment):
    data = {"body":comment}

    http = urllib3.PoolManager()
    encoded_data =json.dumps(data).encode('utf-8')

    request = http.request('POST', "{}sec/v1/insights/{}/comments".format(SUMO_API_URL,id), headers=http_headers, body=encoded_data)
    request_status = request.status

    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        exit()
    else:
        print("\t- Comment added.")

# update insight status
def insight_update_status(id, http_headers, status, resolution):
    data = {"status": status, "resolution": resolution}

    http = urllib3.PoolManager()
    encoded_data =json.dumps(data).encode('utf-8')

    request = http.request('PUT', "{}sec/v1/insights/{}/status".format(SUMO_API_URL, id), headers=http_headers, body=encoded_data)
    request_status = request.status

    if request_status != 200:
        print("Request not accepted. Response code: {}".format(request_status))
        exit()
    else:
        print("\t- Insight closed.")

# main script
if __name__ == '__main__':
    # command line variables handling
    parser = argparse.ArgumentParser(description='A management script for listing and updating CSE Insights')

    # required arguments
    required = parser.add_argument_group('required arguments')
    required.add_argument('-accessid', type=str, nargs=1, help='Sumo Logic API Access ID', required=True)
    required.add_argument('-accesskey',type=str, nargs=1, help='Sumo Logic API Access KEY', required=True)
    required.add_argument('-filter', type=str, nargs=1, help='CSE Insight filter (ex: \'-status="closed" -tag="custom"\')', required=True)

    # optional arguments
    parser.add_argument('-test', action="store_true", help='test mode (no change applied)')
    parser.add_argument('-env', type=str, nargs=1, help='Sumo Logic Environment (default: "us2")')
    parser.add_argument('-tag', type=str, nargs=1, help='new TAG to apply')
    parser.add_argument('-comment', type=str, nargs=1, help='new COMMENT to apply')
    parser.add_argument('-status', type=str, nargs=1, help='new STATUS to apply')
    parser.add_argument('-resolution', type=str, nargs=1,  help='new RESOLUTION to apply')

    args = parser.parse_args()

    # Sumo Logic API Access configuration
    SUMO_API_ACCESS_ID = args.accessid[0]
    SUMO_API_ACCESS_KEY = args.accesskey[0]

    # Sumo Logic instance environment
    if args.env:
        SUMO_API_URL =  "https://api.{}.sumologic.com/api/".format(args.env[0])
    else:
        SUMO_API_URL =  "https://api.us2.sumologic.com/api/"

    # Insights configuration
    INSIGHTS_FILTER = args.filter[0] 
    
    # Test mode
    TEST_MODE =  args.test

    # API authentication and headersconfiguration
    auth= "{}:{}".format(SUMO_API_ACCESS_ID, SUMO_API_ACCESS_KEY)
    headers = urllib3.make_headers(basic_auth=auth)
    headers.setdefault('Content-Type', 'application/json')
    headers.setdefault('Accept', 'application/json')

    # output headers
    print("\nFilter: {}\n".format(INSIGHTS_FILTER))
    print("{:20s} | {:50s} | {:10s} | {:20.20s} | {:20.20s}".format("INSIGHT ID", "NAME", "STATUS", "ENTITY", "ASSIGNEE"))
    print("{:20s} | {:50s} | {:10s} | {:20.20s} | {:20.20s}".format("-" * 20, "-" * 50, "-" * 10, "-" * 20, "-" * 20))

    # main loop
    HAS_NEXT_PAGE = True
    OFFSET = 0
    while HAS_NEXT_PAGE:
        # getting the list of insights
        (insights, HAS_NEXT_PAGE) = get_insights(INSIGHTS_FILTER, headers, OFFSET)

        # looping through insights
        for insight in insights:
            insight_id = insight['readableId']
            insight_name = insight['name']
            insight_status = insight['status']['displayName']
            insight_entity = insight['entity']['name']
            insight_assignee = insight['assignedTo']
            if insight_assignee is None:
                insight_assignee = "NOT ASSIGNED"

            print("{:20s} | {:50s} | {:10s} | {:20.20s} | {:20.20s}".format(insight_id, insight_name, insight_status, insight_entity,insight_assignee ))

            # if test mode is enabled:
            if TEST_MODE:
                print("\t- Test mode enabled - not doing anything.")
                continue

            if args.tag:
                insight_add_tag(insight_id, headers, args.tag[0])
            if args.comment:
                insight_add_comment(insight_id, headers,  args.comment[0])
            if args.status and args.resolution:
                insight_update_status(insight_id, headers, args.status[0], args.resolution[0])

        if HAS_NEXT_PAGE is True:
            print("\nLooping to next page...\n")
            OFFSET += 10








