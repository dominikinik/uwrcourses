using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
/*DOMINIK OLEJARZ
 * VS .NET
 * ZADANIE 2 lista 4*/
namespace POzadanie2lissta4
{

    public class SlowaFibonacciego : IEnumerable<string>
    {
        private readonly int count;

        public SlowaFibonacciego(int count)
        {
            this.count = count;
        }

        public IEnumerator<string> GetEnumerator()
        {
            int n = 1;
            string prev1 = "";
            string prev2 = "";
            while (n <= count)
            {
                string current;
                if (n == 1)
                {
                    current = "b";
                }
                else if (n == 2)
                {
                    current = "a";
                }
                else
                {
                    current = prev1 + prev2;
                }
                yield return current;
                prev2 = prev1;
                prev1 = current;
                n++;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            SlowaFibonacciego sf = new SlowaFibonacciego(6);
            foreach (string s in sf)
            {
                Console.WriteLine(s);
            }

        }
    }
}
