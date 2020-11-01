#!/usr/bin/python
# Jeremy Kosse 10/30/2020
# 
#
#
# - Deletes configuration 
# - This example deletes interface Loopback100
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

# Define Headers for HTTPS request
headers = {
  "Accept": "application/yang-data+json",
  "Content-type": "application/yang-data+json",
}

# Form our URL for the HTTPS request - Configure loopback100
url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"

# Format the request to be sent
response = requests.delete(
  url=url,
  headers=headers, 
  auth=(router['user'], router['password']),
  verify=False
)

# print status_code for debugging
print(f"Status code {response.status_code}")

# Success
if response.status_code == 204:
  print(response.text)
  print("Success")