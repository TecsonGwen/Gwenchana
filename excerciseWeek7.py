"""
Week 7 : Data Serialization - Convert Network Configs
====================================================

Your task: Convert a network device config between JSON and YAML.

FILL IN THE BLANK marked with______
Run this script when done: python exercise_week7.py
"""

import json
import yaml

router_config = {
    "hostname": "Router-1",
    "vendor": "Cisco",
    "interfaces":[
        {"name": "GigabitEthernet1", "ip": "192.168.1.1", "status": "up"},
        {"name": "GigabitEthernet2", "ip": "10.0.0.1", "status": "up"},
        {"name": "GigabitEthernet3", "ip": "172.16.0.1", "status": "down"},

    ]

}





#_____________________________________________________________________________
# EXERCISE 1: Convert Python dict - JSON
#_____________________________________________________________________________
# HINT : converts a python dict to JSON string

print("=== EXERCISE 1 : Convert to JSON ===")

#FILL IN THE BLANK : use to convert router_config to JSON
json_output = json.dumps(router_config, indent=2)

print(json_output)
print()

#===========================================================================
# EXERCISE 2: Convert Python dict -> YAML
#===========================================================================
#Hint: Convert a python dict to a YAML String

print("=== EXERCISE 2: Convert to YAML ===")

# Fill in the BLANK: use to convert router_config to a YAML

yaml_output = yaml.dump(router_config, default_flow_style=False)

print(yaml_output)
print()

#===========================================================================
# EXERCISE 3: Read JSON from a file
#===========================================================================

print("=== EXERCISE 3: Read JSON from a file ===")
#First, let's save our config as a JSON file
with open("router_config.json", "w") as f:
    json.dump(router_config, f, indent=2)

#Now read it back
#FILL IN THE BLANK: use to read from the file
with open("router_config.json", "r") as f:
    
    loaded_config = json.load(f)

print(f"Loaded hostname: {loaded_config['hostname']}")
print(f"Number of interfaces: {len(loaded_config['interfaces'])}")
print()

# The Answer of loaded_config = json.load(f) is 

#===========================================================================
# EXERCISE 4: Save YAML to a file
#===========================================================================
print("=== EXERCISE 4: Save YAML to a file ===")

#FILL IN THE BLANK: open "router_config" for writing
#with open("router_config._____", "_") as f:
with open("router_config.yaml", "w") as f:
    yaml.dump(router_config, f, default_flow_style=False)

print("Saved to router_config.yaml!")
print()

#The Answer is yaml and w

#===========================================================================
# EXERCISE 5: CHALLENGE - Modify and save
#===========================================================================

print("=== EXERCISE 5: CHALLENGE - Modify and save ===")

#Add a new interface (LoopBack0)
new_interface = {"name": "LoopBack0", "ip": "1.1.1.1", "status": "up"}

#FILL IN THE BLANK: append the new interface to the list

router_config["interfaces"].append(new_interface)

#Save updated config
with open("router_config_updated.json", "w") as f:
    json.dump(router_config, f, indent=2)

print(f"Added new interface: {new_interface['name']}")
print(f"Total interfaces now: {len(router_config['interfaces'])}")
print()

print("=" * 50)
print("Exercise Complete! Check your Files:")
print("   - router_config.json")
print("   - router_config.yaml")
print("   - updated_config.json")
print("=" * 50)

# The Answer of the router_config["______"].append(________) is this router_config["interfaces"].append(new_interface)