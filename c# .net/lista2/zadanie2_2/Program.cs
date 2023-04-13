using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace zadanie2_2
{ 
    public static class MathUtils
    {
        public static int Add(int a, int b)
        {
            return a + b;
        }
    }
    /*Modyfikator static dla klas:
    Klasa oznaczona jako static jest niemodyfikowalna i nie może być dziedziczona. 
    Dostęp do elementów składowych klasy static odbywa się poprzez nazwę klasy, a nie poprzez instancję. 
    Klasa static może zawierać tylko składowe static*/
    public class Person6
    {
        public static int Count;
        public string Name;

        public Person6(string name)
        {
            Name = name;
            Count++;
        }
    }
    /*Modyfikator static dla składowych klas (pól, metod):
Modyfikator static dla pól klasowych oznacza, że pole jest współdzielone przez wszystkie instancje klasy, a dostęp do niego odbywa się za pomocą nazwy klasy. 
    Modyfikator static dla metod oznacza, że metoda jest wywoływana bezpośrednio z klasy, a nie z instancji klasy.*/
    public sealed class Rectangle
    {
        public int Width;
        public int Height;

        public Rectangle(int width, int height)
        {
            Width = width;
            Height = height;
        }

        public int GetArea()
        {
            return Width * Height;
        }
    }
    /*Modyfikator sealed dla klas:

  Modyfikator sealed można zastosować do klasy, co oznacza, że klasa nie może być dziedziczona. 
    Klasa oznaczona modyfikatorem sealed nie może mieć klas pochodnych.
    W tym przykładzie klasa Rectangle jest oznaczona modyfikatorem sealed, co oznacza, że nie może mieć klas pochodnych.*/

    public abstract class Shape
    {
        public abstract int GetArea();
    }

    public class Rectangle2 : Shape
    {
        public int Width;
        public int Height;

        public Rectangle2(int width, int height)
        {
            Width = width;
            Height = height;
        }

        public override int GetArea()
        {
            return Width * Height;
        }
    }

    /*Modyfikator abstract dla klas i składowych klas:

    Modyfikator abstract można zastosować do klasy lub składowej klasy, takiej jak metoda, 
    co oznacza, że klasa lub metoda jest niekompletna i musi być zaimplementowana w klasach pochodnych.*/
    public class Shape3
    {
        public virtual void Draw()
        {
            Console.WriteLine("Drawing a shape");
        }
    }

    public class Circle : Shape3
    {
        public override void Draw()
        {
            Console.WriteLine("Drawing a circle");
        }
    }
    /*Słowo kluczowe virtual można zastosować do metody w klasie bazowej, 
     * co oznacza, że metoda może być przesłonięta przez metody pochodne. Słowo
     * kluczowe override można zastosować do metody w klasie pochodnej, co oznacza, 
     * że metoda przesłania metodę w klasie bazowej.W tym przykładzie metoda Draw w 
     * klasie Shape jest oznaczona modyfikatorem virtual, co oznacza, że może być przesłonięta 
     * w klasach pochodnych. Metoda Draw w klasie Circle jest oznaczona modyfikatorem override, 
     * co oznacza, że przesłania metodę Draw w klasie Shape.*/
    public partial class Person
    {
        public string FirstName;
    }

    public partial class Person
    {
        public string LastName;
    }
    /*Słowo kluczowe partial można zastosować do definicji klasy, co oznacza, że definicja klasy 
     jest rozproszona w różnych plikach źródłowych. Klasa może mieć wiele definicji partial, ale 
    muszą one odwoływać się do tej samej klasy.W tym przykładzie klasa Person jest podzielona na
    dwie definicje partial. Jedna definicja zawiera pole FirstName, a druga zawiera pole LastName. 
    Obie definicje odwołują się do tej samej klasy Person.*/
    public class Person3
    {
        public readonly int Id;
        public string Name;

        public Person3(int id, string name)
        {
            Id = id;
            Name = name;
        }
    }
    /*Słowo kluczowe readonly można zastosować do pola klasy, co oznacza, że pole może być 
     * ustawione tylko raz podczas jego inicjalizacji lub w konstruktorze klasy. 
     * Pole oznaczone jako readonly nie może być zmieniane w czasie działania programu.
     W tym przykładzie pole Id jest oznaczone modyfikatorem readonly, co oznacza, że może 
    być ustawione tylko raz w konstruktorze klasy. Pole Name nie jest oznaczone jako readonly 
    i może być zmieniane w czasie działania programu.

Modyfikatory in, ref oraz out na liście parametrów metod:

Modyfikator in oznacza, że parametr jest przekazywany jako wartość wejściowa i nie może być zmieniony wewnątrz metody. Modyfikator ref oznacza, że parametr*/
 

}
internal class Program
{
    static void Main(string[] args)
    {

    }
}
