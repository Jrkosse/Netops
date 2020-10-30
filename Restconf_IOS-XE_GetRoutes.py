#!/usr/bin/python
# Jeremy Kosse 10/30/2020
# 
#
#
# - Gets routing table in XML format 
#
import requests
import json

#Define device information
router = {
    "host": "ios-xe-mgmt.cisco.com",
    "port": "9443",
    "user": "developer",
    "password": "C1sco12345",
}

# Define headers for HTTPS request
headers = {
  "Accept": "application/yang-data+json",
  "Content-type": "application/yang-data+json",
}

# Form the URL used in the HTTPS request
url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-routing:routing"

# Form the request statement
response = requests.get(url=url, headers=headers, auth=(
    router['user'], router['password']), verify=False).json()

# Print the response of the request 
print(json.dumps(response,indent=2))