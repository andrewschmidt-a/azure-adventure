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

def checkpoint1():
    global done, utils
    utils.print_header("Meeting with Dyrk")
    utils.speak("Hey Dyrk! How is your new job at the big tech company!")
    utils.speak("Pretty good! I think I may work there the rest of my life!", "Dyrk")
    utils.speak("Oh cool! I'm glad you're happy!")
    utils.speak("Hey I am trying to prepare for an interview with 3M. Do you have any suggestions for C# interview questions?")
    utils.speak("Why would you use C# as your interview language. I mean I know I'm biased as a Data Scientist but honestly C# has a lot of syntax to remember.", "Dyrk")
    utils.speak("Python is practically Pseudo Code! You would fly through an interview with that!", "Dyrk")
    utils.speak("Hmmmm... thats a good idea. I bet it would be a good language for scripting small things too!")
    utils.speak("Thanks for the tip!")
    utils.speak("Yeah, and make sure you read Cracking the Coding interview! It's Gold!", "Dyrk")
    utils.speak("You bet! It was first on my google search!")

    utils.speak("Hmmm... how hard would it be to learn python now that I know C#...")
    utils.google("Data structures in python")
    utils.textBlock("""
     -------------------------
    |   C#       |   Python   |
    |-------------------------|
    | Array      | list       |
    | Dictionary | dict       |
    | HashSet    | set        |
    | object     | namedtuple |
     -------------------------    
    """)
    utils.speak("Hmm.... doesn't seem that bad!")

    utils.openCode(os.path.join(dir_path, "workspace2"))
    utils.nextCheckpoint()
def checkpoint2():
    global done, utils, dir_path, os

    utils.print_header("HackerRank: Sets")
    utils.speak("This is actually kind of fun! Let's do another one!")
    utils.openCode(os.path.join(dir_path, "workspace3"))

    utils.nextCheckpoint()


def checkpoint3():
    global done, utils, dir_path, os

    utils.print_header("Interview with 3M: Online Screening Question")
    utils.speak("I am ready! It is about time I applied to 3M")
    utils.google("3M CRSL Jobs")
    utils.textBlock("""
    https://www.3m.com/3M/en_US/careers-us/

        + Full Stack Engineer
        + Software Research Engineer
        + Data Scientist
        + Cloud Architect
    """)
    utils.speak("Hmmm... I dont know maybe I'll apply for the Full Stack Engineer position")

    print("...30 min later...\n")
    utils.speak("Oh I got an invitation to participate in the screening process online for 3M's position! Booyah!")
    utils.openCode(os.path.join(dir_path, "screening"))
    utils.speak("Oh wow that is difficult! But they invited me to a phone interview so that someone can work with me to solve a problem.")
    

    utils.nextCheckpoint()
def checkpoint4():
    global done, utils, dir_path, os

    utils.print_header("Interview with 3M: Phone Interview")
    
    print("3M is calling...\n")
    utils.speak("Hello?")
    utils.speak("Hi, my name is Darrel, I am happy to see what you can do!", "Darrel")
    utils.speak("Awesome, how does this work?")
    utils.speak("Well, I'll send you a hackerrank problem and if you haven't seen it before then we'll just dive in. You can share your screen with me", "Darrel")
    utils.speak("Awesome, thanks!")

    utils.openCode(os.path.join(dir_path, "phone_interview"))
    utils.speak("Great job! We'll let you know if you qualify for an on-site! Thanks again", "Darrel")
    utils.nextCheckpoint()
        
def checkpoint5():
    global done, utils, dir_path, os

    utils.print_header("Interview with 3M: The Big Day!")
    utils.speak("Woah, I can't believe it! I am finally here sitting in a 3M conference room...")
    utils.speak("I am really glad my friend took me to the Maplewood nature centre before this. My nerves are doing a lot better...")
    
    utils.speak("My name is Benjamin, nice to meet you!", "Benjamin")
    utils.speak("Yeah, likewise! How do we get started?")
    utils.speak("Well, I just have a couple whiteboard problems if thats okay and then you can tell me more about yourself!")
    utils.speak("Great!")
    utils.speak("Okay the first one is about Binary Search Trees. I just want you to implement a simple insert!", "Benjamin")
    
    utils.openCode(os.path.join(dir_path, "interview"))
    
    utils.speak("Great Job! Now for the hard one! This is a probelm about traversing a tree. Iwant to you to implement Huffman decoding. Its a simple yet effective way to compress data based on probability of the characters occurance.", "Benjamin")

    utils.openCode(os.path.join(dir_path, "interview2"))

    utils.speak("Well done! Now its just the easy part of talking about yourself...", "Benjamin")

    utils.nextCheckpoint()

def checkpoint6():
    global done, utils, dir_path, os

    utils.print_header("Texting Amy")

    utils.speak("Hey Amy! I got the job at 3M!!!")
    utils.speak("Whatt?? really? thats so cool Andrew! I bet your exhausted!", "Amy")
    utils.speak("Yeah, I can't believe how long of a road that was! But now I'm just relaxing with a fresh Bannana Creme Pie!")
    utils.speak("Wow, nicely done! You deserve it!", "Amy")
    utils.speak("Do you have time to catch up?")
    utils.speak("I have a really important exam this week but yeah perhaps on friday night?", "Amy")
    utils.speak("Sounds great!")
    utils.speak("It will be so good to see you! ttyl!", "Amy")

    print("...\n")

    utils.speak("I can't believe it is finished. In a few weeks I'll be an engineer with 3M!")
    utils.speak("Then the real learning can begin!")

    utils.nextModule("interview")
    done = True
def main(checkpoint, common_utils):
    global done, utils
    utils = common_utils
    while not done:
        eval("checkpoint"+str(checkpoint)+"()")
        checkpoint += 1
        utils.add_checkpoint("interview", checkpoint)