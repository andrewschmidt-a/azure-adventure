import sqlite3, os, subprocess
from markdown import markdown
import re
clear = lambda: os.system('clear') #on Linux System
def add_checkpoint(module, checkpoint):
    conn = sqlite3.connect('state.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO checkpoints(module, number) VALUES (?,?)''', (module,checkpoint))
    conn.commit()
    cur.close()
def speak(sentance, person="You"):
    print("{}: {}".format(person, sentance))
    input()
def print_header(header):
    print(header)
    print('=' * len(header)+"\n")
def textBlock(string):
    print(string)
    input()

def nextCheckpoint():
    input("\nClick any key to continue...")
    clear()
def openCode(path):
    printREADME(path)
    print("Click Enter to open your workspace....")
    input()
    subprocess.call(["code", path])
    waitLoop(path)
    
def waitLoop(path):
    printHelp()
    while True:
        selection = input()
        if selection == 'done':
            break
        elif selection == 'help':
            printHelp()
        elif selection == 'instruction':
            printREADME(path)
        else:
            print("Invalid command! type 'help' to get usage info\n")
        print("\n")
def printHelp():
    print ("""
type one of the following keywords:
'done' when you are finished
'instruction' to print what you are supposed to do
'help' for this message
""")

def getModules():
    return ['intro', 'dotnet']
def nextModule(currentModule):
    modules = getModules()
    index = modules.index(currentModule)

    # if theres is another module left then add checkpoint
    if len(modules) >index+1:
        add_checkpoint(modules[index+1], 0)

def google(text):
    text += " " * (34-len(text))
    textBlock(r"""

                _____                   _      
               / ____|                 | |     
              | |  __  ___   ___   __ _| | ___ 
              | | |_ |/ _ \ / _ \ / _` | |/ _ \
              | |__| | (_) | (_) | (_| | |  __/
               \_____|\___/ \___/ \__, |_|\___|
                                   __/ |       
                                  |___/        
 ___________________________________     ________________
|                                   |   |                |
| """          +text+           r"""|   |     Search     |
|___________________________________|   |________________|


""")

def printREADME(path):
    global os

    f=open(os.path.join(path, "README.md"),"r")
    print("\n\n"+f.read()+"\n")
    f.close()
