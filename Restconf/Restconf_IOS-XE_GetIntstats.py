#!/usr/bin/python
# Jeremy Kosse 10/30/2020
# 
#
#
# - Gets interface stats from an IOS-XE device
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
    router['username'], router['password']), verify=False).json()

# Convert data to JSON and print output
print(json.dumps(response,indent=2))