#config.py

#
import json

#
def getConfig(attribute):
    with open("Config/Config.json", "r") as Config:
        attributes = json.load(Config)
        return attributes[attribute]
    
#
