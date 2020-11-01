#!/usr/bin/python
# Jeremy Kosse 10/26/2020
# 
#
#
# - Find the device capabilities for Netconf
#
#
from ncclient import manager

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

# Initialize the manager as M and only keep the session open while we print capabilities.
with manager.connect(**router, hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print(capability)
