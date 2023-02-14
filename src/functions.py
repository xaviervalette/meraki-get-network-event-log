import json

def writeToJsonFile(filepath, dataJson):
    with open(filepath, "w") as outfile:
        json.dump(dataJson, outfile)