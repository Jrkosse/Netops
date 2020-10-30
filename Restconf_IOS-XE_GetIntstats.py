#!/usr/bin/python
# Jeremy Kosse 10/30/2020
# 
#
#
# - Gets interface stats from an IOS-XE device
#
import requests
import json

# Define our device
router = {
    "host": "ios-xe-mgmt.cisco.com",
    "port": "9443",
    "user": "developer",
    "password": "C1sco12345",
}

# Define the headers for the HTTP request
headers = {
  "Accept": "application/yang-data+json",
  "Content-type": "application/yang-data+json",
}

# Define the URL -  Get stats for a specific Interface
# url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

# Define the URL - Get stats for all interfaces
url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/"

# Form our request and assign the output to response
response = requests.get(url=url, headers=headers, auth=(
    router['user'], router['password']), verify=False).json()

# Convert data to JSON and print output
print(json.dumps(response,indent=2))