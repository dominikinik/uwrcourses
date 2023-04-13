using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
namespace _4_5
{
    internal class Program
    {
        static void Main(string[] args)
        {
            var daneOsobowe = File.ReadLines("plik1.txt")
                      .Select(linia => linia.Split(' '))
                      .Select(wyrazy => new { Imie = wyrazy[0], Nazwisko = wyrazy[1], PESEL = wyrazy[2] });

            var daneFinansowe = File.ReadLines("plik2.txt")
                                   .Select(linia => linia.Split(' '))
                                   .Select(wyrazy => new { PESEL = wyrazy[0], NumerKonta = wyrazy[1] });

            var danePolaczone = from osoba in daneOsobowe
                                join finanse in daneFinansowe on osoba.PESEL equals finanse.PESEL
                                select new { Imie = osoba.Imie, Nazwisko = osoba.Nazwisko, PESEL = osoba.PESEL, NumerKonta = finanse.NumerKonta };

            foreach (var rekord in danePolaczone)
            {
                Console.WriteLine($"{rekord.Imie} {rekord.Nazwisko} {rekord.PESEL} {rekord.NumerKonta}");
            }
        }
    }
}
