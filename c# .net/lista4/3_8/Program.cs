using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3_8
{
    class Program
    {
        public static Func<A, R> Y<A, R>(Func<Func<A, R>, Func<A, R>> f)
        {
            Func<A, R> g = null;
            g = f(a => g(a));
            return g;
        }
        public static void Main()
        {
            List<int> list = new List<int>() { 1, 2, 3, 4, 5 };
            Func<int, int> recursiveDelegate = Y<int, int>(e => x => (x <= 2) ? 1 : e(x - 2) + e(x - 1));
            foreach (var v in list.Select(i => recursiveDelegate(i)))
            {
                Console.WriteLine(v);
            }
        }
    }
}
