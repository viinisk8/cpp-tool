#runObject

#
import json
import subprocess
import os

#
from FunctionsLib import config

#
def runImplementation():
    with open("Config/Files.json", "r") as f:
        data = json.load(f)

    files = data["files"]
    joined_files = " ".join([f'"{file}"' for file in files])

    output_dir = "Build"
    exe_path = "Build/program.exe"

    os.makedirs(output_dir, exist_ok=True)

    vcvars = '"C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Auxiliary/Build/vcvars64.bat"'

    #
    command = (
        f'cmd.exe /c "{vcvars} && '
        f'cl /Fo{output_dir}/ /Fe{exe_path} {joined_files}"'
    )

    subprocess.run(command, shell=True)