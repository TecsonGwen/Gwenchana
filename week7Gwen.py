import json
import yaml
import os

try:
    import xmltodict
    HAS_XMLTODICT =True
except ImportError:
    HAS_XMLTODICT = False
    print("Note: xmltodict not installed. Run: pip install xmltodict")

ROUTER_CONFIG = {
    "device": {
        "hostname": "Router-1",
        "vendor": "Cisco",
        "model": "CSR1000V",
        "version": "16.12.04",
        "interfaces": [
            {
                "name": "GigabitEthernet1",
                "ip_address": "192.168.1.1",
                "subnet_mask": "255.255.255.0",
                "status": "up",
                "description": "Manager Interface",
            },
            {
                "name": "GigabitEthernet2",
                "ip_address": "192.168.2.1",
                "subnet_mask": "255.255.255.0",
                "status": "up",
                "description": "WAN Link to ISP",
            },
            {
                "name": "GigabitEthernet3",
                "ip_address": "192.168.3.1",
                "subnet_mask": "255.255.255.0",
                "status": "up",
                "description": "Backup Link",
            },
            {
                "name": "Loopback0",
                "ip_address": "1.1.1.1",
                "subnet_mask": "255.255.255.255",
                "status": "up",
                "description": "Loopback Interface",
            },
        ],
       "routing": {
            "ospf": {
                "process_id": 1,
                "router_id": "1.1.1.1",
                "networks": [
                    {"network": "192.168.1.0", "wildcard": "0.0.0.255", "area": 0},
                    {"network": "10.0.0.0", "wildcard": "0.0.0.3", "area": 0}
                ]
            },
            "bgp": {
                "asn": 65001,
                "neighbors": [
                    {"ip": "10.0.0.2", "remote_as": 65002}
                ]
            }
        },
        "services": {
            "ntp": "192.168.1.100",
            "dns": "0.0.0.0",
            "ssh_enabled": 2
        }
    }
}

def to_json(data, indent=4):
    """Convert dictionary to JSON String."""
    return json.dumps(data, indent=indent)

def to_yaml(data):
    """Convert dictionary to YAML String."""
    return yaml.dump(data, default_flow_style=False, sort_keys=False)

def to_xml(data, root_tag = "config"):
    """Convert dictionary to XML String."""
    if not HAS_XMLTODICT:
        raise ("xmltodict is not installed. Run: pip install xmltodict")
    return xmltodict.unparse({root_tag: data}, pretty=True)

def validate_json(json_string):
    """Validate JSON syntax and return parsed data."""
    try:
        data = json.loads(json_string)
        return True, data
    except json.JSONDecodeError as e:
        return False, str(e)

def validate_yaml(yaml_string):
    """Validate YAML syntax and return parsed data."""
    try:
        data = yaml.safe_load(yaml_string)
        return True, data
    except yaml.YAMLError as e:
        return False, str(e)

def confirm_configs(json_data, yaml_data, xml_data):
    """Confirm two config dictionaries for equality."""
    return json.dumps(json_data, sort_keys=True) == json.dumps(yaml_data, sort_keys=True)

def main():
    print("=" * 60)
    print("Week 7 : Data Serialization Formats ")
    print("Network Device Configuration Conversion")
    print("=" * 40)
    
    #show original config 
    print("\n1. Original COnfiguartion (Python Dict):")
    print("-" * 40)
    print(json.dumps(ROUTER_CONFIG, indent=2))

    #convert to JSON
    json_output = to_json(ROUTER_CONFIG)
    print("\n2. JSON Format:")
    print("-" * 40)    
    print(json_output)

      #convert to YAML
    yaml_output = to_yaml(ROUTER_CONFIG)
    print("\n3. YMAL Format:")
    print("-" * 40)
    print(yaml_output)

      #convert to XML
    if HAS_XMLTODICT:
     xml_output = to_xml(ROUTER_CONFIG)
     print("\n3. XML Format:")
     print("-" * 40)
     print(xml_output)

     #Validation exercise
    print("\n5. Validation Exercise: ")
    print("-" * 40)

      # Valid JSON
    valid_json = '{"hostname": "Test"}'
    is_validate, result = validate_json(valid_json)
    print(f"Valid JSON: {is_validate} -> {result}")

    #Valid YAML
    valid_yaml = '{"hostname": "Test"}'
    is_validate, result = validate_yaml(valid_json)
    print(f"Valid YAML: {is_validate} -> {result}")

    #validation challenge

    # Validation challenge
    print("\n6. Challenge: Validate this config file")
    print("-" * 40)
    challenge_config = """
device:
  hostname: Router-2
  interfaces:
    - name: eth0
      ip: 192.168.1.10
    - name: eth1
      ip: 10.0.0.10
"""
    is_valid, result = validate_yaml(challenge_config)
    print(f"Challenge config valid: {is_valid}")
    if is_valid:
        print(f"Parsed hostname: {result['device']['hostname']}")
        print(f"Number of interfaces: {len(result['device']['interfaces'])}")

    print("\n" + "=" * 60)
    print("Exercise Complete!")
    print("Try modifying ROUTER_CONFIG and running again")
    print("=" * 60)


if __name__ == "__main__":
    main()

     
     




