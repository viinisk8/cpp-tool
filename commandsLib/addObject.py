#add

#
import json
import os
import keyboard

#
from FunctionsLib import config
from FunctionsLib import output

#
def addImplementation():
    def terminal_folder_browser(start_path):
        current_path = os.path.abspath(start_path)
        selected_index = 0
        stack = []
        window_size = 10  # Número de itens visíveis no terminal

        def list_dirs(path):
            try:
                return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
            except PermissionError:
                return []

        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            dirs = list_dirs(current_path)
            print(f"Navegando em: {current_path}")
            print("Use ↑ ↓ para mover, W para entrar, A para voltar, E para selecionar, Q para sair\n")

            if not dirs:
                print("Nenhuma subpasta.")
            else:
                start_index = max(0, selected_index - window_size // 2)
                end_index = min(len(dirs), start_index + window_size)

                for i in range(start_index, end_index):
                    prefix = ">> " if i == selected_index else "   "
                    print(f"{prefix}{dirs[i]}")

            event = keyboard.read_event()
            if event.event_type != "down":
                continue

            key = event.name

            if key == 'up':
                selected_index = (selected_index - 1) % len(dirs) if dirs else 0
            elif key == 'down':
                selected_index = (selected_index + 1) % len(dirs) if dirs else 0
            elif key == 'w':
                if dirs:
                    stack.append(current_path)
                    current_path = os.path.join(current_path, dirs[selected_index])
                    selected_index = 0
            elif key == 'a':
                if stack:
                    current_path = stack.pop()
                    selected_index = 0
            elif key == 'e':
                if dirs:
                    selected_folder = os.path.join(current_path, dirs[selected_index])
                    return selected_folder
            elif key == 'q':
                return None
                
            
    selected = terminal_folder_browser(os.path.join(config.getConfig('directory')))
    print(selected)

    objectName = input("Enter with the file's name:  ")
    cpp = f'{selected}/{objectName}.cpp'
    h = f'{selected}/{objectName}.h'

    with open(h, "w") as arquivo:
        arquivo.write(f'//{objectName}.h\n\n//\nclass {objectName} {{\n\n}};')
        output.FileCreated(h)

    with open(cpp, "w") as arquivo:
        arquivo.write(f'//{objectName}.cpp\n\n//\n#include "{objectName}.h"')
        output.FileCreated(cpp)
    #
    Objects = f'{config.getConfig('directory')}/Config/Files.json'

    if not os.path.exists(Objects):
        print("Objects.json not found")
    
    else:
        with open(Objects, "r+", encoding="utf-8") as f:
            dados = json.load(f)
            completedcpp = f'{cpp.replace('\\', '/')}'
            if cpp not in dados["files"]:
                dados["files"].append(completedcpp)
                f.seek(0)
                json.dump(dados, f, indent=4)
                f.truncate()