import lixo.data as data
import os

def start_implementation():
    print("Starting your project")
    print("----------------------------------")
    data.ProjectName = input("Put the name of your project: ")

    # 
    with open(f"{data.Directory}/{data.ProjectName}.cpp", "w") as arquivo:
        arquivo.write(data.GetCppInitialContent(data.ProjectName))

    #
    for f in data.InitialFolders:
        os.makedirs(f)

    #
    with open(data.Objects, "w") as arquivo:
        caminho = f"{data.Directory.replace('\\', '/')}/{data.ProjectName}.cpp"
        arquivo.write(f'{{\n    "files": [\n        "{caminho}"\n    ]\n}}')

    #
    with open(data.Link, "w") as arquivo:
        arquivo.write(f'{{\n    "Libs": [\n  ]\n}}')