#!/usr/bin/python
# Jeremy Kosse 10/26/2020
# 
#
#
# - Get basic interface information from a Cisco IOS-XE device
# - This script gets both operational and configuration state data
#
from ncclient import manager
import xmltodict
import pprint

#Define device information
router = {
  "host": "ios-xe-mgmt.cisco.com",
  "port": "10000",
  "username": "developer",
  "password": "C1sco12345"
}

# Define our XML filter
int_filter = """
  <filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>GigabitEthernet2</name>
      </interface>
    </interfaces>
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>GigabitEthernet2</name>
      </interface>
    </interfaces-state>
  </filter>
"""
# Connect to the device
with manager.connect(**router, hostkey_verify=False) as m:
  # Issue our GET RPC and parse it with our int_filter
  netconf_response = m.get(int_filter)
  # Take the netconf_response and convert the XML into a python dictionary
  # Further refine the RPC-Reply/Data as that is not needed.
  python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
  # To get Operaitional information use interfaces-state 
  op = python_response["interfaces-state"]["interface"]
  # To get configuration information use interfaces.
  config = python_response["interfaces"]["interface"]
  
  # Use the below to see all the responses/data that comes back
  # Use the Yang template to find the wanted variables. 
  # For example...
  print(f"Name: {config['name']['#text']}")
  print(f"Desc: {config['description']}")
  print(f"Enabled: {config['enabled']}")
  # print(f"Enabled: {config['ipv4']['address']['ip']}")
  print(f"Status: {op['admin-status']} / {op['oper-status']}")
  print(f"MAC: {op['phys-address']}")
  print(f"Speed: {op['speed']}")