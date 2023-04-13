using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _3_5
{
    public static class ListHelper
    {
        public static List<TOutput> ConvertAll<T, TOutput>(List<T> list, Converter<T, TOutput> converter)
        {
            List<TOutput> result = new List<TOutput>(list.Count);
            for (int i = 0; i < list.Count; i++)
            {
                result.Add(converter(list[i]));
            }
            return result;
        }

        public static List<T> FindAll<T>(List<T> list, Predicate<T> match)
        {
            List<T> result = new List<T>();
            for (int i = 0; i < list.Count; i++)
            {
                if (match(list[i]))
                {
                    result.Add(list[i]);
                }
            }
            return result;
        }

        public static void ForEach<T>(List<T> list, Action<T> action)
        {
            for (int i = 0; i < list.Count; i++)
            {
                action(list[i]);
            }
        }

        public static int RemoveAll<T>(List<T> list, Predicate<T> match)
        {
            int count = 0;
            for (int i = list.Count - 1; i >= 0; i--)
            {
                if (match(list[i]))
                {
                    list.RemoveAt(i);
                    count++;
                }
            }
            return count;
        }

        public static void Sort<T>(List<T> list, Comparison<T> comparison)
        {
            list.Sort(comparison);
        }
    }


    internal class Program
    {
        static void Main(string[] args)
        {
        }
    }
}
