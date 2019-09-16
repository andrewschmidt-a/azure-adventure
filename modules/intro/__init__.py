import os 

utils = {}
done = False
dir_path = os.path.dirname(os.path.realpath(__file__))

def checkpoint0():
    global done, utils
    utils.print_header("May 5, 2018: The University of Nebraska commencement")
    utils.speak("Congratulations! You have a degree that will take you far and wide.", "Chancellor Ron Vert")
    utils.speak("Well done! I loved having you in my data structures class, and I'm sure you will do well in your career!", "Professor Patrick Rhine")
    utils.speak("We're so happy for you!", "Aunt Laraine")
    utils.speak("Hey cuz, great to see you made it through!", "Scott")
    utils.speak("Excellent Job! You better keep studying Data Compression for your new jobs cause I can tell you that Arithmetic encoder you wrote was hardly efficient!", "Professor Winston Sood")

    utils.nextCheckpoint()

def checkpoint1():
    global done, utils
    utils.print_header("Later that night while texting Amy")
    utils.speak("I can't believe I am done!")
    utils.speak("Yeah, way to rub it in, my college gets out next week!", "Amy")
    utils.speak("Right, and you are just heading back for 4 more years of medical school!")
    utils.speak("Yeah...(sigh)...guess I'm just a glutton for punishment", "Amy")
    utils.speak("Heyyy, where is it that you are going to work now??", "Amy")
    utils.speak("Well, yeah I really should have focused on that more. Hopefully I can find a good Job!")
    utils.speak("Hmmm. Have you thought about applying at 3M?? Its a pretty good company and they do Software Research! Plus if you get the job you could live up here by me (;", "Amy")
    utils.speak("That would be so cool!")
    utils.speak("Hey my dad is calling me to sort out some things. ttyl?", "Amy")
    utils.speak("Okay goodnight!")
    utils.nextCheckpoint()

def checkpoint2():
    global done, utils, os, dir_path
    utils.print_header("The next day during a job search")
    utils.google("Most popular coding languages")
    utils.textBlock("""
Top 3:
==================
Node Js
+++++++
Python
+++++++
C#
+++++++
""")  
    utils.speak("Hmmm.... I know it is always good to know a strongly typed language. Maybe I'll start with C#. All they taught me in school was Java!")
    
    utils.openCode(os.path.join(dir_path, "workspace"))
    
    utils.speak("Woah, that wasnt too bad. I'm glad I know a little C# now! But I better get to some harder stuff!")
    utils.nextCheckpoint()

def checkpoint3():
    global done, utils, os, dir_path
    utils.print_header("Learning C# Basics")

    utils.speak("I wonder what it would be like to actually use numbers in C#")
    utils.openCode(os.path.join(dir_path, "workspace2"))
    utils.nextCheckpoint()

def checkpoint4():
    global done, utils, os, dir_path
    utils.print_header("Learning C# Basics")

    utils.speak("Now I know how to do Loops in Java... what about C#??")
    utils.openCode(os.path.join(dir_path, "workspace3"))
    utils.nextCheckpoint()

def checkpoint5():
    global done, utils, os, dir_path
    utils.print_header("Learning C# Basics")

    utils.speak("Okay, now I need to be able to use Arrays!")
    utils.openCode(os.path.join(dir_path, "workspace4"))
    utils.nextCheckpoint()

    done = True
    utils.nextModule("intro")


def main(checkpoint, common_utils):
    global done, utils
    utils = common_utils
    while not done:
        eval("checkpoint"+str(checkpoint)+"()")
        checkpoint += 1
        utils.add_checkpoint("intro", checkpoint)
