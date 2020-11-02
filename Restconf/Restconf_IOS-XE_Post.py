#!/usr/bin/python
# Jeremy Kosse 10/30/2020
# 
#
#
# - Uses the POST method to add a configuration
#
import requests
import json

# Welcome
print("Welcome to the Netconf_IOS-XE_Post.py Script!")
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
  auth=(router['username'], router['password']),
  data=json.dumps(payload),
  verify=False
)

# Print status code for debugging
print(f"Status code {response.status_code}")

# Acceptance 
if response.status_code == 201:
  print(response.text)
  print("Success")