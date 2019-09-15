using System.Collections.Generic;
using System;

namespace linq_challenge
{
    class Program
    {
        static List<string> GetList(string SQLitePath){
            throw new NotImplementedException(); // delete this line
            return new List<string>();
        }
        static void Main(string[] args)
        {
            foreach(string person in Program.GetList("employees.db")){
                Console.WriteLine(person);
            }
            Console.ReadLine(); // just so the console doesnt quit
        }
    }
}
