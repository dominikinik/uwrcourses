using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using ClassLibrary1;

namespace zdanie
{
    internal class Program
    {

        static void Main(string[] args)
        {
            Wektor v1 = new Wektor(3);
            v1.wspolrzedne[0] = 1;
            v1.wspolrzedne[1] = 2;
            v1.wspolrzedne[2] = 3;

            Wektor v2 = new Wektor(3);
            v2.wspolrzedne[0] = 4;
            v2.wspolrzedne[1] = 5;
            v2.wspolrzedne[2] = 6;

            Wektor v3 = v1 + v2;
            float iloczyn = v1 * v2;
            Wektor v4 = 2.5f * v1;
            float norma = v1.Norma();
        }
    }
}
