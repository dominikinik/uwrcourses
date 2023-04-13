using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lista3
{
    public interface IClassInfo
    {
        string[] GetFieldNames();
        object GetFieldValue(string fieldName);
    }

    public class Person : IClassInfo
    {
        public string Name { get; set; }
        public string Surname { get; set; }

public string[] GetFieldNames()
        {
            return new[] { "Name", "Surname" };
        }
        public object GetFieldValue(string fieldName)
        {
            switch (fieldName)
            {
                case "Name":
                    return this.Name;
                case "Surname":
                    return this.Surname;
                default:
                    return null;
            }
            throw new NotImplementedException();
        }
    }
    public class XMLGenerator
    {
        public string GenerateXML(IClassInfo dataObject)
        {
            StringBuilder sb = new StringBuilder();
            sb.Append($"<{dataObject.GetType().Name}>");

            foreach (string fieldName in dataObject.GetFieldNames())
            {
                object fieldValue = dataObject.GetFieldValue(fieldName);
                if (fieldValue != null)
                {
                    sb.Append($"<{fieldName}>{fieldValue}</{fieldName}>");
                }
            }

            sb.Append($"</{dataObject.GetType().Name}>");
            return sb.ToString();
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Person person = new Person()
            {
                Name = "Jan",
                Surname = "Kowalski"
            };

            XMLGenerator generator = new XMLGenerator();
            string xml = generator.GenerateXML(person);
            Console.WriteLine(xml);
        }
    }
}
