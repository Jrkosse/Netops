#!/usr/bin/python
# Jeremy Kosse 10/26/2020
# 
#
#
# - Get basic BGP information from an IOS-XE device using Netconf
#
#
from ncclient import manager
import xmltodict
import pprint

# Define device information
router = {
  "host": "ios-xe-mgmt.cisco.com",
  "port": "10000",
  "username": "developer",
  "password": "C1sco12345",
}

# Define XML filter and Yang model
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

# Run the internal code while we're connected to the device
with manager.connect(**router, hostkey_verify=False) as m:
  # Use GET and pass the XML filter in
  netconf_response = m.get(int_filter)
  # Convert the XML resopnse into a python dictionary
  python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
  # Pull specific data points
  op = python_response["bgp-state-data"]["neighbors"]["neighbor"]
  # Use the below to see all the responses/data that comes back
  # pprint.pprint(python_response)
  print(f"Name: {op['neighbor-id']}")
  print(f"Session-State: {op['session-state']}")
  print(f"Link: {op['link']}")
