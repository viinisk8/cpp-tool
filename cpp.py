#cpp.py

import commands

def GetCommand():
    par = input("---> Enter with the command: ")

    if par in commands.dic:
        commands.dic[par]()
        GetCommand()

    else:
        print("Unknown command")
        GetCommand()

#
GetCommand()