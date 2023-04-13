using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Xml;

namespace _3_3
{
    public interface IClassInfo
    {
        string[] GetFieldNames();
        object GetFieldValue(string fieldName);
    }
    [AttributeUsage(AttributeTargets.Property)]
    public class IgnoreInXMLAttribute : Attribute
    {
    }
    public class Person : IClassInfo
    {
        public string Name { get; set; }
        [IgnoreInXML]
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
            Type type = dataObject.GetType();
            PropertyInfo[] properties = type.GetProperties();

            sb.Append($"<{type.Name}>");

            foreach (PropertyInfo property in properties)
            {
                if (Attribute.IsDefined(property, typeof(IgnoreInXMLAttribute)))//dodane
                {
                    continue;
                }
                object propertyValue = property.GetValue(dataObject);
                if (propertyValue != null)
                {
                    sb.Append($"<{property.Name}>{propertyValue}</{property.Name}>");
                }
            }

            sb.Append($"</{type.Name}>");
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
