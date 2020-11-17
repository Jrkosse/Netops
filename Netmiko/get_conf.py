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
    with open('devices.csv') as csvfile:
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
       
    # Define output file attributes - Creates a file called ip_counters_md.txt E.g, 192.168.86.107_counters_0932.txt
    now = datetime.now() # Current date/time
    month = now.strftime("%m")
    day = now.strftime("%d")
    base_name = "config"
    extension = ".txt"
    separator = "_"
    full_file = str(ip) + separator + base_name + separator + month + day + extension

    # Connect to the device
    net_connect = ConnectHandler(**device_dict)

    # Run the command 
    pager_command = net_connect.send_command("terminal pager 0")
    configuration_output = net_connect.send_command("show run")

    # Define separation for when the file is appended
    sep_output = "******************** Date: {} {} ********************\n".format(month,day)
    # Open the above defined file and write the output of the command to the file and close it.
    f = open(full_file, mode="a")
    f.write(sep_output)
    f.write(configuration_output)
    f.close()

        
# Start the python program    
if __name__ == "__main__":
    main()
    print("Script Complete!")