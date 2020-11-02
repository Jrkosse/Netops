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

# Welcome
print("Welcome to the Netconf_IOS-XE_Delete.py Script!")
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
  auth=(router['username'], router['password']),
  verify=False
)

# print status_code for debugging
print(f"Status code {response.status_code}")

# Success
if response.status_code == 204:
  print(response.text)
  print("Success")