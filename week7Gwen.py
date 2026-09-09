import json
import yaml
import os

try:
    import xmltodict
    HAS_SMLTODICT =True
except ImportError:
    HAS_SMLTODICT = False
    print("Note: xmltodict not installed. Run: pip install xmltodict")