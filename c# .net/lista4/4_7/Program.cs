using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _4_7
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var item = new { Field1 = "q", Field2 = 5 };
            Console.WriteLine(item.Field1);
            var item1 = new { Field1 = "w", Field2 = 5 };
            var item2 = new { Field1 = "e", Field2 = 10 };
            List<object> theList = new List<object> { item1, item2 };
         
            theList.Add(new { Field1 = "r", Field2 = 15 });
        }
    }
}
