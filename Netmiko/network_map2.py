import csv
from datetime import datetime
from getpass import getpass
from netmiko import ConnectHandler

def gather_devices(u,p):
    # Open the referenced file. File contains list of devices and their details.
    with open('Netmiko/devices.csv') as csvfile:
        # Read over the file
        readCSV = csv.reader(csvfile,delimiter=',')
        # For each row in the CSV file - If first row(0) is ip, then run the function to test ping the IP.
        # This allows for dynamic addresses/networks while allowing remarks in the file
        for row in readCSV:
            if row[0] == 'ip':
                # Call the Run device function
                connect(row[2],row[3],u,p)
            elif row[0] == 'eof':
                break


def connect(os,ip,u,p):
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
        # Add commands here cisco_ios_show_ip_route_summary.textfsm, .*, cisco_ios, sh[[ow]] ip ro[[ute]] sum[[mary]]
        show_ip_route = net_connect.send_command("sh ip ro sum", use_textfsm=True)
        print(show_ip_route)



        # Gracefully Disconnect from the device
        net_connect.disconnect()
    except Exception as ex:
        print(ex)
    else:
        # Define separation for when the file is appended
        sep_output = f"\n******************** {ip} ********************\n"
        # Open the above defined file and write the output of the command to the file and close it.
        # f = open(full_file, mode="a")
        # f.write(sep_output)   
        # parsed_show_ip_route.pop(0)

        # for i in range(0,number_of_routes):
        #   f.write(parsed_show_ip_route[i])


        # f.close()
        # print("Routes retrieved for: {}".format(ip))



def process_data():
    print("Processes and formats data")

def output():
    print("Final output")


# Starts the program
# Welcome print - Collect credentials
print("-" * 50)
print("Welcome to the Network Map script")
print("-" * 50)
u = input("Username: ")
p = getpass("SSH Password: ")
print("-" * 50)
gather_devices(u,p)