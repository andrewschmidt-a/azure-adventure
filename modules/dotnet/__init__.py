import os 

utils = {}
done = False
dir_path = os.path.dirname(os.path.realpath(__file__))

def checkpoint0():
    global done, utils
    utils.print_header("Eating Sushi with your friend Jake")
    utils.speak("Hey Jake! I saw you got a job at a startup! Congrats!")
    utils.speak("Yeah I am so excited!! Where are you going to be this next year??", "Jake")
    utils.speak("I am actually currently trying to prepare for my interviews with 3M!")
    utils.speak("Oh wow! Thats really cool! They are a great company to work for!", "Jake")
    utils.speak("Yeah I know so I am trying to get some programming skills sharpened, I am working on C# now")
    utils.speak("That's really cool!! You using LINQ yet?? That library makes C# the best thing I have ever used!", "Jake")
    utils.speak("No I haven't used it yet, what is it??")
    utils.speak("Its a Data processing library, it helps you do Maps, Reduces, Filters and more on your data sets. I honestly can't believe people use C# without it.", "Jake")
    utils.speak("Thanks for telling me about it! I'll have to look into it.")
    utils.speak("Yeah, just promise me you wont stay on C# forever. Its great but you need to just jump in and interview with companies. You could 'prepare' forever...", "Jake")
    utils.speak("Thanks again, I'll keep that in mind. I know I have some basics to learn but I'll try not to get stuck")
    utils.speak("Yeah man, I got to go! I have an Ultimate match soon and I don't have my car so it will take me a bit to skate to campus!", "Jake")
    utils.speak("Okay! Goodbye Jake!")

    utils.nextCheckpoint()

def checkpoint1():
    global done, utils, dir_path, os

    utils.print_header("Back at home and ready to study!")
    utils.google("C# .NET LINQ")
    utils.textBlock("""
https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/

Language Integrated Query (LINQ)
================================
Language-Integrated Query (LINQ) is the name for a set of technologies based on the integration of query capabilities directly into the C# language. Traditionally, queries against data are expressed as simple strings without type checking at compile time or IntelliSense support. Furthermore, you have to learn a different query language for each type of data source: SQL databases, XML documents, various Web services, and so on. With LINQ, a query is a first-class language construct, just like classes, methods, events. You write queries against strongly typed collections of objects by using language keywords and familiar operators. The LINQ family of technologies provides a consistent query experience for objects (LINQ to Objects), relational databases (LINQ to SQL), and XML (LINQ to XML).
    """)

    utils.speak("Wow Jake wasnt kidding, this is pretty cool!")
    utils.textBlock("""
class LINQQueryExpressions
{
    static void Main()
    {
        
        // Specify the data source.
        int[] scores = new int[] { 97, 92, 81, 60 };

        // Define the query expression.
        IEnumerable<int> scoreQuery =
            from score in scores
            where score > 80
            select score;

        // Execute the query.
        foreach (int i in scoreQuery)
        {
            Console.Write(i + " ");
        }            
    }
}
// Output: 97 92 81
    """)
    utils.speak("Wow! I can't believe how easy that was... I wonder if it is well preforming...")

    utils.speak("Woah, I can connect many sources and query across DTO relationships! Thats's so cool! I better start out with something simple though!")

    utils.openCode(os.path.join(dir_path, "workspace"))
    utils.nextCheckpoint()

def checkpoint2():
    global done, utils, dir_path, os

    utils.print_header("Challenge: LINQ")
    utils.speak("I wonder if I can connect this to a database!")
    utils.google("C# LINQ sqlite")
    utils.textBlock("""
To help LINQ to SQL work with SQLite, pass the connection object to create the DataContext object. The connection string for SQLite database is simple. It has the format of Data Source= <Path of the file>. The connection string is the only difference from any other LINQ to SQL implementation.
    """)
    utils.speak("Cool I can't wait to figure this out!")

    utils.openCode(os.path.join(dir_path, "challenge"))
    utils.nextCheckpoint()


def checkpoint3():
    global done, utils, dir_path, os

    utils.print_header("Making my first Web API")
    utils.speak("Playing around with all this is really cool. But I would really like to make something real!")
    utils.google("C# Web API project")
    utils.textBlock("""
https://docs.microsoft.com/en-us/learn/modules/build-web-api-net-core/
Create a RESTful service with ASP.NET Core that supports Create, Read, Update, Delete (CRUD) operations.
========================================================================================================

In this module, you will:

    Create a web API project with ASP.NET Core.
    Create an in-memory database for persisting products.
    Add support for CRUD operations.
    Test web API action methods from the command shell.
Prerequisites
    Experience writing C# at the beginner level
    Familiarity with RESTful service concepts and HTTP action verbs, such as GET, POST, PUT, and DELETE
    """)
    utils.speak("Oh neat! This is a full tutorial! And I get XP points on Microsoft Learn!")
    utils.openCode(os.path.join(dir_path, "workspace2"))
    utils.nextCheckpoint()

def checkpoint4():
    global done, utils, dir_path, os

    utils.print_header("Talking to Professor Jerome")
    utils.speak("Hey Professor Jerome! How are you doing? Getting ready for the design class?")
    utils.speak("Yeah, its going to be a busy year! Lots of corporate sponsors", "Jerome")
    utils.speak("Thats great! Hey I'm trying to study C# for my interviews and wondering if you had any ideas of what to learn??")
    utils.speak("Just what I told you for 4 years to practise! Unit testing and Dependency Injection! These are the two greatest tools in your toolkit. They help you write solid code!", "Jerome")
    utils.speak("Yeah I know I was looking it up and saw that there are many types of Unit Test frameworks. What would you go with? MSTest, Nunit or Xunit?")
    utils.speak("I would just use MSTest for now. It's the easiest to get going. However I think Nunit is more widely used.", "Jerome")
    utils.speak("Oh great! Thanks so much. What about Dependency Injection frameworks? Ninject, Autofac or Unity?")
    utils.speak("Well actually I think thats a native feature for C# now... let me check!", "Jerome")
    utils.google("C# .NET Core Dependency Injection")
    utils.speak("Yeah it says they've had it since .NET Core 2.1. I would again just go with that as its the easiest to get going with. You may goto a company and find that they use another. Likely it will be for historical reasons but perhaps they use the more mature features of other frameworks.", "Jerome")
    
    utils.speak("Awesome! Thanks so much!")

    utils.openCode(os.path.join(dir_path, "challenge2"))
    utils.nextCheckpoint()
    
def checkpoint5():
    global done, utils, dir_path, os

    utils.print_header("Unit Testing")
    utils.speak("I guess I should look at testing. (sigh)")

    utils.openCode(os.path.join(dir_path, "workspace3"))
    
    utils.nextModule("dotnet")
    done = True
def main(checkpoint, common_utils):
    global done, utils
    utils = common_utils
    while not done:
        eval("checkpoint"+str(checkpoint)+"()")
        checkpoint += 1
        utils.add_checkpoint("dotnet", checkpoint)