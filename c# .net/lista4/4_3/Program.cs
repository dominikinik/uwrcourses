using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace _4_3
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var firstLetters = File.ReadAllLines("plik.txt")
                      .Select(name => name.Substring(0, 1))
                      .OrderBy(letter => letter)
                      .Distinct()
                      .ToList();

            foreach (var letter in firstLetters)
            {
                Console.WriteLine(letter);
            }
        }
    }
}
