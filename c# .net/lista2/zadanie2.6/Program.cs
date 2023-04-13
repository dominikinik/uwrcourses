using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace zadanie2._6
{/*eśli zdarzenie ma informować o każdej zmianie wartości każdej właściwości, to można zdefiniować jedno zdarzenie o ogólniejszej sygnaturze. 
  * Jeśli jednak chcemy mieć więcej kontroli nad tym, które właściwości są obserwowane, można stworzyć osobne zdarzenia dla każdej właściwości.*/
    public class Person
    {
        private string name;
        private string surname;

        public delegate void PropertyValueChangedEventHandler(object source, string propertyName, object propertyValue);

        public event PropertyValueChangedEventHandler PropertyValueChanged;

        public string Name
        {
            get { return name; }
            set
            {
                if (value != name)
                {
                    name = value;
                    OnPropertyValueChanged("Name", value);
                }
            }
        }

        public string Surname
        {
            get { return surname; }
            set
            {
                if (value != surname)
                {
                    surname = value;
                    OnPropertyValueChanged("Surname", value);
                }
            }
        }

        protected virtual void OnPropertyValueChanged(string propertyName, object propertyValue)
        {
            PropertyValueChanged?.Invoke(this, propertyName, propertyValue);
        }


        /*Jeśli chcemy, aby powiadomienie pojawiało się zawsze, kiedy nadana jest wartość właściwości, należy 
         * wywoływać zdarzenie PropertyValueChanged w każdym akcesorze set. Jeśli jednak chcemy, aby powiadomienie 
         * pojawiało się tylko wtedy, kiedy nowa wartość pola jest różna od poprzedniej, należy dodać odpowiednie warunki, 
         * jak to zostało zrobione w przykładzie powyżej.*/
        private static void Person_PropertyValueChanged(object source, string propertyName, object propertyValue)
        {
            Console.WriteLine("właściwość {0}, nowa wartość {1}", propertyName, propertyValue);
        }

        static void Main(string[] args)
        {

            Person person = new Person();
            person.PropertyValueChanged += Person_PropertyValueChanged;
            person.Name = "Jan";
            person.Surname = "Kowalski";
                person.Surname = "Kowalski";
            person.Surname = "nikt";
            
            Console.ReadLine();
        }
    }
    

 

}
