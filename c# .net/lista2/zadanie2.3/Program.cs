using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace zadanie2._3
{
    internal class Program
    {
        /*Przeciążanie sygnatur funkcji:*/
        public static void Print(string message)
        {
            Console.WriteLine(message);
        }

        public static void Print(int number)
        {
            Console.WriteLine($"Number: {number}");
        }

        public static void Print(double number)
        {
            Console.WriteLine($"Number: {number}");
        }
        /* Typ zwracany z funkcji przeciążonych może być różny:*/
        public static int Add(int a, int b)
        {
            return a + b;
        }

        public static double Add(double a, double b)
        {
            return a + b;
        }
        /*Funkcja przeciążona może wywołać inną funkcję przeciążoną zamiast dostarczać własnej implementacji:*/
        public static void Print2(string message)
        {
            Console.WriteLine(message);
        }

        public static void Print2(int number)
        {
            Print2(number.ToString()); // wywołuje metodę Print(string) zamiast dostarczać własnej implementacji
        }

        /*Funkcja może wywołać funkcję z klasy bazowej zamiast dostarczać własnej implementacji:*/
        public class Animal
        {
            public virtual void Speak()
            {
                Console.WriteLine("I am an animal.");
            }
        }

        public class Dog : Animal
        {
            public override void Speak()
            {
                base.Speak(); // wywołuje metodę Speak z klasy bazowej (Animal)
                Console.WriteLine("I am a dog.");
            }
        }
        /*Przeciążanie konstruktorów klasy:*/
        public class Person
        {
            public string FirstName { get; set; }
            public string LastName { get; set; }
            public int Age { get; set; }

            public Person()
            {
                FirstName = "John";
                LastName = "Doe";
                Age = 30;
            }

            public Person(string firstName, string lastName)
            {
                FirstName = firstName;
                LastName = lastName;
                Age = 30;
            }

            public Person(string firstName, string lastName, int age)
            {
                FirstName = firstName;
                LastName = lastName;
                Age = age;
            }
        }


        static void Main(string[] args)
        {
            
        Print("Hello, world!"); // wywołuje metodę Print(string)
        Print(42); // wywołuje metodę Print(int)
        Print(3.14); // wywołuje metodę Print(double)


            int result1 = Add(1, 2); // wywołuje metodę Add(int, int) i zwraca wynik typu int (3)
            double result2 = Add(2.5, 3.5); // wywołuje metodę Add(double, double) i zwraca wynik typu double (6.0)


            Print2("Hello, world!"); // wywołuje metodę Print(string)
            Print2(42); // wywołuje metodę Print(int), która z kolei wywołuje metodę Print(string)



            Animal animal = new Dog();
            animal.Speak(); // wywołuje metodę Speak z klasy Dog, która z kolei wywołuje metodę Speak z klasy bazowej (Animal)


            Person person1 = new Person(); // wywołuje konstruktor Person() i tworzy obiekt z domyślnymi wartościami pól
            Person person2 = new Person("Jane", "Doe"); // wywołuje
        }
    }
}
