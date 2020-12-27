import sqlite3
from dc import get_data

# Get the data and insert into the db
def insert_vlan(data):
    with conn:
        # Formatting 
        data_split = data.split('\n')
        # Setting default variables
        vlan_id = ""
        vlan_desc = ""
        vlan_gw = ""
        # Go through each line, pick out the interesting data, assing to variables
        for lines in data_split:
            if lines.startswith("interface") == True:
                vlan_id = lines.split(" ")[1]
            if lines.startswith(" desc") == True:
                vlan_desc = lines
            if lines.startswith(" ip address") == True:
                vlan_gw = lines

        # Check to see if Vlan is already in the database. 
        c.execute("SELECT ROWID FROM vlans WHERE vlan_id =:vlan_id", {"vlan_id":vlan_id})
        if len(c.fetchall()) == 0:
            print(f"No existing vlan - {vlan_id} Adding to database")
            # If not in the DB - insert
            c.execute("INSERT INTO vlans VALUES (:vlan_id,:vlan_desc,:vlan_gw)",
            {'vlan_id':vlan_id,
            'vlan_desc':vlan_desc,
            'vlan_gw':vlan_gw})
            # If it's already in the DB - skip
        else:
            print(f"{vlan_id} already found - Skipping")

# Create the connection to the DB. 
conn = sqlite3.connect('vlans.db')
c = conn.cursor()

# Test for existing DB
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='vlans' ''')
if c.fetchone()[0]==0:
    print('Table does not exist.')
    # Create Data base
    print("Creating Database")
    #conn = sqlite3.connect(':memory:')
    conn = sqlite3.connect('vlans.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE vlans (vlan_id text, vlan_desc text, vlan_gw text)""")
    print("Database Created")
else:
    print('Connecting to existing DB')

# Call the db.py script and run the get_data() method. This will connect to the device and pull the information.
data = get_data()

# For each item of data run the insert_vlan() function. 
for i in data:
    insert_vlan(i)

# Gracefully close our connection to the database. 
conn.close()