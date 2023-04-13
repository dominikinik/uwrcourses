using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using jakasbiblioteka;


namespace lista2_1
{
    public class COS
    {
        public string Name;

        private int Age;

        internal bool absolwent;

        protected double Avg;
        public COS(string name, int age, bool absolwent, double avg)
        {
            Name = name;
            Age = age;
            this.absolwent = absolwent;
            Avg = avg;
        }

        public void hello()
        {
            Console.WriteLine($"elo jestem {Name}");
        }
        private void zwiekszeniewieku()
        {
            Age++;
        }
        internal void zdal()
        {
            absolwent = true;
        }
        protected void zmianasredniej(double sred)
        {
            Avg = sred;
        }
        public void polaczenie(double sred)
        {
            zwiekszeniewieku();
            zmianasredniej(sred);

        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            var os = new COS("jan", 19, false, 4.23);
            Console.WriteLine(os.Name);
            //Console.WriteLine(os.Age);
            Console.WriteLine(os.absolwent);
           // Console.WriteLine(os.Avg);
            os.hello();
            //os.zwiekszeniewieku();
            //os.zmianasredniej(4.90);
            double pom = 4.9;
            os.polaczenie(pom);
            var auto = new AUTO("audi", "1990", 3, "1999");
            Console.WriteLine(auto.nazwa);
            //Console.WriteLine(auto.rok);
            //Console.WriteLine(auto.iloscwalscicieli);
            // Console.WriteLine(auto.perrejestracja);
/*public - Konstruktor publiczny jest dostępny z poziomu dowolnego miejsca w kodzie, zarówno wewnątrz klasy, 
 * jak i z zewnątrz. Konstruktor ten może być wywoływany przez wszystkie klasy i metody, które mają dostęp do klasy,
 * w której znajduje się konstruktor. Konstruktor publiczny jest często używany do tworzenia nowych obiektów klasy.

protected - Konstruktor chroniony jest dostępny tylko wewnątrz klasy, w której się znajduje, oraz wewnątrz klas pochodnych. 
Konstruktor ten nie może być wywoływany z poziomu innych klas w tym samym projekcie lub z zewnątrz projektu. 
Konstruktor chroniony jest często używany do zapewnienia, że tylko klasy pochodne mogą tworzyć instancje klasy bazowej.

internal - Konstruktor wewnętrzny jest dostępny tylko w obrębie tej samej przestrzeni nazw, co klasa, w której się znajduje.
Konstruktor ten nie może być wywoływany z poziomu innych przestrzeni nazw lub z zewnątrz projektu. 
Konstruktor wewnętrzny jest często używany do tworzenia instancji klasy wewnątrz projektu.

private - Konstruktor prywatny jest dostępny tylko wewnątrz klasy, w której się znajduje. 
Konstruktor ten nie może być wywoływany z poziomu innych klas w tym samym projekcie lub z zewnątrz projektu.
Konstruktor prywatny jest często używany do zapobiegania tworzenia instancji klasy z zewnątrz klasy.*/





}
}
}
