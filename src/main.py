# Import the required libraries:
# requests: for sending HTTP requests
# json: for encoding and decoding JSON data
# time: for sleeping the script in case of too many requests
import requests
import json
import time
from functions import *
import yaml
from datetime import datetime


# Open the config.yml file and load its contents into the 'config' variable
with open('config.yml', 'r') as file:
    config = yaml.safe_load(file)

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": config["apiKey"]
}

# Loop through each network defined in the config file
for network in config["networks"]:
    url = f"https://api.meraki.com/api/v1/networks/{network['networkId']}/events?productType={network['productType']}&perPage={network['perPage']}"
    payload = None
    response = requests.request('GET', url, headers=headers, data = payload)
    now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    writeToJsonFile(filepath=config["logFolder"]+now+"_"+network["filename"], dataJson=response.json())

