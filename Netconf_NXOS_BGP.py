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

# Define device information
router = {
  "host": "sbx-nxos-mgmt.cisco.com",
  "port": "10000",
  "username": "admin",
  "password": "Admin_1234!"
}

# Define our XML filter
int_filter = """
  <filter>
    <bgp-state-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-bgp-oper">
      <neighbors>
        <neighbor>
        </neighbor>
      </neighbors>    
    </bgp-state-data> 
  </filter>
"""
# Connect to the device
with manager.connect(**router, hostkey_verify=False) as m:
  # Issue our GET RPC and parse it with our int_filter
  netconf_response = m.get(int_filter)
  # Take the netconf_response and convert the XML into a python dictionary
  # Further refine the RPC-Reply/Data as that is not needed.
  python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
  # Operational state data
  op = python_response["bgp-state-data"]["neighbors"]["neighbor"]
  # Use the below to see all the responses/data that comes back and reference
  # The yang model to find other variables you may need.
  print(f"Name: {op['neighbor-id']}")
  print(f"Session-State: {op['session-state']}")
  print(f"Link: {op['link']}")
