#!/usr/bin/python
# Jeremy Kosse 10/28/2020
# 
#
#
# - Uses Restconf to connect to a device and print it's capabilities
#
import requests
import json

# Welcome
print("Welcome to the Netconf_IOS-XE_BGP.py Script!")
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

# Format our URL to make the API call
url = f"https://{router['host']}:{router['port']}/restconf/data/netconf-state/capabilities"

# Set our headers
headers = {
  "Accept": "application/yang-data+json",
  "Content-type": "application/yang-data+json",
}

# Use the requests library, pass in URL, headers, auth, and key_checking
response = requests.get(url=url,headers=headers,auth=(router['username'],router['password']), verify=False)

# If response is good, print a list of the capabilities
if response.status_code == 200:
    response_dict = response.json()
    for capability in response_dict['ietf-netconf-monitoring:capabilities']['capability']:
      print(capability)