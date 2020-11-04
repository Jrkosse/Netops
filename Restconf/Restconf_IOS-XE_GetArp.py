#!/usr/bin/python
# Jeremy Kosse 11/4/2020
# 
#
#
# - Gets ARP table in XML format 
# 
import requests
import json

# Welcome
print("Welcome to the Netconf_IOS-XE_GetArp.py Script!")
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

# Form the URL used in the HTTPS request
url = f"https://{router['host']}:{router['port']}/restconf/data/Cisco-IOS-XE-arp-oper:arp-data/arp-vrf?fields=arp-oper(interface;address;hardware)"

# Form the request statement
response = requests.get(url=url, headers=headers, auth=(
    router['username'], router['password']), verify=False).json()

# Print the response of the request 
print(json.dumps(response,indent=2))