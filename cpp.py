#cpp.py

import actions
import sys

actions.data.Directory = sys.argv[1]
Par = ""
Commands = ["start", "finish", "add", "run"]
CommandsActions = {
    "start": actions.start,
    "finish": actions.finish,
    "add": actions.add,
    "run": actions.run
}

# --------------------------------------------------------------
def GetCommand():

    #
    global Par
    Par = input(actions.data.ProjectName + "  ---> Enter with the command: ").lower()

    #
    if Par not in Commands:
        print("Unknown command")
        GetCommand()
    else:
        CommandsActions[Par]()
        GetCommand()

# --------------------------------------------------------------

### run
GetCommand()

    