import csv
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler


def main():
    # Welcome print - Collect credentials
    print("-" * 50)
    print("Welcome to the configuration backup script!\nUse this to capture a configuration to file.\nPlease verify SSH is working prior to running script")
    print("-" * 50)
    u = input("Username: ")
    p = getpass("SSH Password: ")
    print("-" * 50)
    # Open the referenced file. File contains list of devices and their details.
    with open('Netmiko/devices.csv') as csvfile:
        # Read over the file
        readCSV = csv.reader(csvfile,delimiter=',')
        # For each row in the CSV file - If first row(0) is ip, then run the function to test ping the IP.
        # This allows for dynamic addresses/networks while allowing remarks in the file
        for row in readCSV:
            if row[0] == 'ip':
                # Call the Run device function
                run_device(row[2],row[3],u,p)
            elif row[0] == 'eof':
                break
# Each device will have this ran 
def run_device(os,ip,u,p):
    # Define the devices into a dictionary of which netmiko likes
    device_dict = {
        'device_type': os,
        'host': ip,
        'username': u,
        'password': p,
    }
       
    # Define output file attributes 
    full_file = "routes.txt"

    # Begin connecting to the device
    try:
        # Connect to the device
        net_connect = ConnectHandler(**device_dict)

        # Run the command 
        net_connect.send_command("terminal pager 0")
        # Add commands here
        show_ip_route = net_connect.send_command("show ip route connected | i C")
        # Cleanup the output
        parsed_show_ip_route = show_ip_route.split("\n")

        number_of_routes = len(parsed_show_ip_route) - 1
        # Gracefully Disconnect from the device
        net_connect.disconnect()
    except Exception as ex:
        print(ex)
    else:
        # Define separation for when the file is appended
        sep_output = f"\n******************** {ip} ********************\n"
        # Open the above defined file and write the output of the command to the file and close it.
        f = open(full_file, mode="a")
        f.write(sep_output)   
        parsed_show_ip_route.pop(0)

        for i in range(0,number_of_routes):
          f.write(parsed_show_ip_route[i])


        f.close()
        print("Routes retrieved for: {}".format(ip))

        
# Start the python program    
if __name__ == "__main__":
    main()
    print("-" * 50)
    print("Script Complete!")
    print("-" * 50)