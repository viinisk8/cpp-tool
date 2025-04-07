#startImplementation

#
import os
import json

#
from FunctionsLib import output
from FunctionsLib import config

#
def startImplementation():
    
    #
    projectName = input("Put the name of your project: ")
    directory = os.getcwd()

    #
    os.makedirs("Config", exist_ok=True)
    output.FolderCreated("Config")

    os.makedirs("Source", exist_ok=True)
    output.FolderCreated("Source")

    os.makedirs("Libs", exist_ok=True)
    output.FolderCreated("Libs")

    os.makedirs("Build", exist_ok=True)
    output.FolderCreated("Build")

    #
    with open("Config/Config.json", "w") as f:
        obj = {
            "directory": directory,
            "projectName": projectName
        }
        
        json.dump(obj, f, indent=4)
        output.FileCreated(f'Config/Config.json')

    with open("Config/Files.json", "w") as f:
        cpp = f'{projectName}.cpp'
        obj = {
            "files": [cpp]
        }

        json.dump(obj, f, indent=4)
        output.FileCreated("Config/Files.json")
    
    with open("Config/Libs.json", "w") as f:
        obj = {
            "libs": []
        }

        json.dump(obj, f, indent=4)
        output.FileCreated("Config/Libs.json")

    #
    with open(f'{config.getConfig('projectName')}.cpp', "w") as f:
        content = f'//{config.getConfig('projectName')}\n\n int main() {{\n\n}}'
        f.write(content)