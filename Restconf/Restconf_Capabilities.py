#!/usr/bin/python
# Jeremy Kosse 10/28/2020
# 
#
#
# - Uses Restconf to connect to a device and print it's capabilities
#
import requests
import json

# Define device information
router = {
    "host": "ios-xe-mgmt.cisco.com",
    "port": "9443",
    "user": "developer",
    "password": "C1sco12345",
}

# Format our URL to make the API call
url = f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"

# Set our headers
headers = {
  "Accept": "application/yang-data+json",
  "Content-type": "application/yang-data+json",
}

# Use the requests library, pass in URL, headers, auth, and key_checking
response = requests.get(url=url,headers=headers,auth=(router['user'],router['password']), verify=False)

# If response is good, print a list of the capabilities
if response.status_code == 200:
    response_dict = response.json()
    for capability in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
      print(capability)