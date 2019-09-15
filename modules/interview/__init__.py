import os 

utils = {}
done = False
dir_path = os.path.dirname(os.path.realpath(__file__))

def checkpoint0():
    global done, utils
    utils.print_header("Data Structures: HashMaps")
    utils.speak("Cool, I think I have learned a lot of important things about C#! I think I am ready to start prepping for the interviews!")
    utils.google("interview prep")
    utils.textBlock("""
+ Cracking the Coding Interview by Gayle Lockland McDowell
+ Interviewing in Python
+ LeetCode
+ HackerRank
    """)
    utils.speak("There is a lot of cool things to do to prepare!")
    utils.speak("Maybe I'll start with a HackerRank question")
    utils.openCode(os.path.join(dir_path, "workspace"))
    utils.nextCheckpoint()
    
def checkpoint5():
    global done, utils, dir_path, os

    utils.print_header("Unit Testing")
    utils.speak("I guess I should look at testing. (sigh)")

    utils.openCode(os.path.join(dir_path, "workspace3"))
    
    utils.nextModule("interview")
    done = True
def main(checkpoint, common_utils):
    global done, utils
    utils = common_utils
    while not done:
        eval("checkpoint"+str(checkpoint)+"()")
        checkpoint += 1
        utils.add_checkpoint("interview", checkpoint)