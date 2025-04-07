from commandsLib import startObject
from commandsLib import finishObject
from commandsLib import addObject

def start():
    startObject.startImplementation()

def finish():
    finishObject.finishImplementation()

def add():
    addObject.addImplementation()

#
dic = {
    "start": start,
    "finish": finish,
    "add": add
}