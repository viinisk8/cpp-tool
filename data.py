#DATA

# variables

ProjectName = " "
Directory = " "

InitialFolders = ["Source", "Config", "Build", "Libs"]
Link = f'Config/Link.json'
Objects = f'Config/Objects.json'
DeveloperCommand = f'"C:/Program Files/Microsoft Visual Studio/2022/Community/VC/Auxiliary/Build/vcvars64.bat"'

# ------------------------------------------------------------------------------------------------------------------------------ Main file content.
def GetCppInitialContent(ParProjectName):
    return f'// {ParProjectName}.cpp\n\n#include <iostream>\n\nint main() {{\n  std::cout << "Hello World" << std::endl;\n}}'

# ------------------------------------------------------------------------------------------------------------------------------ 