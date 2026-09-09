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
    "hostaname": "Router-1",
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