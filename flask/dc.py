import json
from napalm import get_network_driver

# This will get called from the db.py script.
def get_data(): 
    """ Primary Method called from db.py """ 
    def get_interfaces():
        """Take output, use json functions to convert into a usable dictionary"""
        ios_output = iosvl2.get_facts()
        ios_output_str = json.dumps(ios_output, sort_keys=True, indent=4)
        ios_output_dict = json.loads(ios_output_str)
        dev_list = []
        # Iterate through each vlan config snip
        for int in ios_output_dict['interface_list']:
            if 'Vlan' in int:
                dev_list.append(int)
        return(dev_list)


    # Connect to the device
    driver = get_network_driver('ios')
    iosvl2 = driver('192.168.86.29', 'cisco', 'cisco')
    iosvl2.open()
    print("Connection opened to device")

    # Run the get_interfaces function and assign it to device_list
    device_list = get_interfaces()
    # Set blank string variable
    final_output = []

    # For each vlan the get_facts() function called, run 'show run int vlan' to pull the full config
    for i in device_list:
        command = [f'show run int {i}']    
        full_int_conf = iosvl2.cli(command)
        for k in full_int_conf:
            # Get the show run int configuration, removing the last 3 chars (end)
            formatted_conf = full_int_conf[k].split("!")[1]
            final_output.append(formatted_conf[1:-3])
    # Gracefully close the connection to the device.
    iosvl2.close()
    return(final_output)




