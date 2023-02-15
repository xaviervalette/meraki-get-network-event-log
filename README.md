# Meraki Network Event Log collector

## What is it ?
A solution that helps you to quickly collect the logs of ```Network-wide > Event Log```. If you use the ```Download as > CSV``` button, you will download only the 30 events that are displayed on the page:

<img width="" alt="image" src="https://user-images.githubusercontent.com/28600326/218786336-73f17349-1815-42cd-a3ba-93e9aed8c655.png">

If you need to get more, you will need to collect the logs 30 by 30 by clicking on ```older >>``` and then ```Download as > CSV```.

To face this limitation, you can use the following python script to collect, via API, the Event Logs of Meraki Networks (up to 1000 at once).

## Prerequisites
- Meraki Dashboard access
- Meraki API key
- Meraki network ID

## Get started
1. Clone or download this repo
2. Add a file called config.yml as follow:
```diff
└── meraki-network-event-log-collector/
+   ├── config.yml
    └── src/
    │    ├── functions.py
    │    └── main.py  
    └── log/
```
3. In the variables.py file, add the following variables:
```yaml
#config.yml
---
apiKey: "<yourApiKey>"
logFolder: "<yourLogFolder>"
networks:
  # This is the 1st network in the list.
  - networkId: "<yourNetworkId1>"
    filename: "network1.log"
    productType: "wireless"
    perPage: <1-1000>
    
  # ...

  # This is the Nth network in the list.
  - networkId: <yourNetworkIdN>
    filename: "networkN.log"
    productType: "wireless"
    perPage: <1-1000>
...

```
ⓘ You can change the filenames and productTypes to match your needs

4. Now you can run the code by using the following command:
```console
python3 <your_workpath>/meraki-network-event-log-collector/main.py
```

## Output
The output should be as followed:
```diff
└── meraki-network-event-log-collector/
    ├── config.yml
    └── src/
    │    ├── functions.py
    │    └── main.py  
    └── log/
+        ├── network1.log
+        ├── ...
+        └── networkN.log
    
```
Example:
```json
#network1.log
{
     "message": null,
     "pageStartAt": "2023-02-14T07:03:26.537131Z",
     "pageEndAt": "2023-02-14T15:16:31.501370Z",
     "events": [
          {
               "occurredAt": "2023-02-14T13:10:18.749327Z",
               "networkId": "L_00000000000000000",
               "type": "wpa_auth",
               "description": "WPA authentication",
               "clientId": "0000000",
               "clientDescription": "iPhone-13-Pro-Max-de-XVA",
               "clientMac": "00:00:00:00:00:00",
               "deviceSerial": "0000-0000-0000",
               "deviceName": "MR44-VIR-1",
               "ssidNumber": 1,
               "ssidName": "SFR_9990_5GHZ",
               "eventData": {}
          },
          {
               "occurredAt": "2023-02-14T13:10:18.732346Z",
               "networkId": "L_00000000000000000",
               "type": "association",
               "description": "802.11 association",
               "clientId": "0000000",
               "clientDescription": "iPhone-13-Pro-Max-de-XVA",
               "clientMac": "00:00:00:00:00:00",
               "deviceSerial": "0000-0000-0000",
               "deviceName": "MR44-VIR-1",
               "ssidNumber": 1,
               "ssidName": "SFR_9990_5GHZ",
               "eventData": {
                    "channel": "56",
                    "rssi": "45"
               }
          },

          ...
```



