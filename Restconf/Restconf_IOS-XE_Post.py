#!/usr/bin/python
# Jeremy Kosse 10/30/2020
# 
#
#
# - Uses the POST method to add a configuration
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

# Form our URL to configure the loopback interface
url = f"https://{router['host']}:{router['port']}/restconf/data/ietf-interfaces:interfaces/"

# Configure the payload - typical interface configuration
payload = {
  "ietf-interfaces:interface": {
    "name": "Loopback100",
    "description": "Added By KAP",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "192.168.55.1",
          "netmask": "255.255.255.0"
        }
     ]
    },
  }
}

# Form the HTTPS POST request 
response = requests.post(
  url=url,
  headers=headers, 
  auth=(router['user'], router['password']),
  data=json.dumps(payload),
  verify=False
)

# Print status code for debugging
print(f"Status code {response.status_code}")

# Acceptance 
if response.status_code == 201:
  print(response.text)
  print("Success")