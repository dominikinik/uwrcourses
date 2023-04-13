using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3_4
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> numbers = new List<int> { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

            List<string> strings = numbers.ConvertAll(delegate (int num) { return num.ToString(); });
            Console.WriteLine(string.Join(", ", strings)); 

          
            List<int> evenNumbers = numbers.FindAll(delegate (int num) { return num % 2 == 0; });
            Console.WriteLine(string.Join(", ", evenNumbers)); 

            numbers.ForEach(delegate (int num) { Console.Write(num + " "); }); 

            numbers.RemoveAll(delegate (int num) { return num > 5; });
            Console.WriteLine("\n" + string.Join(", ", numbers));

            numbers.Sort(delegate (int x, int y) { return y.CompareTo(x); }) ; 
            Console.WriteLine(string.Join(", ", numbers)); 
        }
    }
}
