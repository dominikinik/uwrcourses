using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace _4_2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var numbers = File.ReadAllLines("plik.txt")
                  .Select(line => int.Parse(line))
                  .Where(number => number > 100)
                  .OrderByDescending(number => number);

            foreach (var number in numbers)
            {
                Console.WriteLine(number);
            }
            var numbers2 = File.ReadAllLines("plik.txt")
                  .Select(line => int.Parse(line))
                  .Where(number => number > 100)
                  .OrderByDescending(number => number)
                  .ToList();

            foreach (var number in numbers2)
            {
                Console.WriteLine(number);
            }
        }
    }
}
