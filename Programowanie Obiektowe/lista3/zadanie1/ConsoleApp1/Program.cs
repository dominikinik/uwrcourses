using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ClassLibrary1;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Lista<int> lista = new Lista<int>();

            lista.push_front(1);
            lista.push_front(2);
            lista.push_back(3);

            Console.WriteLine(lista.pop_front());
        }
    }
}
