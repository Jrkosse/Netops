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

# Welcome
print("Welcome to the Netconf_IOS-XE_Put.py Script!")
print("*" * 80)

# Variable collection
host_value = input("Host: ")
port_value = input("Port: ")
username = input("Username: ")
password = input("Password: ")

# Define the device and pull vars from user input
router = {
    "host":host_value,
    "port": port_value,
    "username": username,
    "password": password,
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
  auth=(router['username'], router['password']),
  data=json.dumps(payload),
  verify=False
)

# Print the status code for debugging
print(f"Status code {response.status_code}")

# Acceptance response
if response.status_code == 201:
  print(response.text)
  print("Success")