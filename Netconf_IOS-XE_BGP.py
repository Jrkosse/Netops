#!/usr/bin/python
# Jeremy Kosse 10/26/2020
# 
#
#
# - Get basic BGP information from an IOS-XE device using Netconf
#
#
from ncclient import manager
#import logging
import xmltodict
import pprint

# logging.basicConfig(level=logging.DEBUG)

router = {
  "host": "ios-xe-mgmt.cisco.com",
  "port": "10000",
  "username": "developer",
  "password": "C1sco12345"
}

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
with manager.connect(**router, hostkey_verify=False) as m:
  netconf_response = m.get(int_filter)
  python_response = xmltodict.parse(netconf_response.xml)["rpc-reply"]["data"]
  op = python_response["bgp-state-data"]["neighbors"]["neighbor"]
  # Use the below to see all the responses/data that comes back
  # pprint.pprint(python_response)
  print(f"Name: {op['neighbor-id']}")
  print(f"Session-State: {op['session-state']}")
  print(f"Link: {op['link']}")
