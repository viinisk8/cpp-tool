from commandsLib import startObject
from commandsLib import finishObject
from commandsLib import addObject
from commandsLib import runObject

def start():
    startObject.startImplementation()

def finish():
    finishObject.finishImplementation()

def add():
    addObject.addImplementation()

def run():
    runObject.runImplementation()

#
dic = {
    "start": start,
    "finish": finish,
    "add": add,
    "run": run
}