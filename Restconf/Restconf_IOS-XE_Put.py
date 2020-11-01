#!/usr/bin/python
# Jeremy Kosse 10/30/2020
# 
#
#
# - Uses the PUT HTTPS method to add/update a configuration
# - In this example updating the IP of loopback100 
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

# Define headers for HTTPS request
headers = {
  "Accept": "application/yang-data+json",
  "Content-type": "application/yang-data+json",
}

# Define the URL used in the PUT method
url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"

# Define our payload - This is a typical interface configuration
payload = {
  "ietf-interfaces:interface": {
    "name": "Loopback100",
    "description": "AUTOMATED BY KPI",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "172.18.79.1",
          "netmask": "255.255.255.0"
        }
     ]
    },
  }
}

# Form our request and assign the output to response
response = requests.put(
  url=url,
  headers=headers, 
  auth=(router['user'], router['password']),
  data=json.dumps(payload),
  verify=False
)

# Print the status code for debugging
print(f"Status code {response.status_code}")

# Acceptance response
if response.status_code == 201:
  print(response.text)
  print("Success")