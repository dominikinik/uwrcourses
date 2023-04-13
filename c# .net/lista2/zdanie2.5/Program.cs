using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace zdanie2._5
{
    /*za pomoca get i set
     Person posiada prywatne pole "name", do którego dostęp jest kontrolowany za pomocą właściwości "Name". 
    Właściwość "Name" zawiera get i set, które pozwalają na odczytanie i zapisanie wartości pola "name". 
    Właściwość ta posiada pole kopii zapasowej "name", które przechowuje wartość pola.*/
    public class Person
    {
        private string name;

        public string Name
        {
            get { return name; }
            set { name = value; }
        }
    }
    /* Person posiada właściwość "Name", która jest implementowana automatycznie.
     * W tym przypadku nie ma potrzeby definiowania pola kopii zapasowej, ponieważ C# automatycznie generuje je dla nas.
     * Właściwość "Name" ma jedynie get i set, które pozwalają na odczytanie i zapisanie wartości pola.*/
    public class Person2
    {
        public string Name { get; set; }
    }

    internal class Program
    {

        static void Main(string[] args)
        {
        }
    }
}
