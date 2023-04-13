using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace lista4
{
    public static class StringExtensions
    {
        public static bool IsPalindrome(this string str)
        {
    
            string cleanStr = new string(str.ToLower().Where(c => !char.IsPunctuation(c) && !char.IsWhiteSpace(c)).ToArray());


            for (int i = 0; i < cleanStr.Length / 2; i++)
            {
                if (cleanStr[i] != cleanStr[cleanStr.Length - 1 - i])
                {
                    return false;
                }
            }

            return true;
        }
    }


    internal class Program
    {
        
        static void Main(string[] args)
        {
        string s = "Kobyła ma mały bok.";
       Console.WriteLine(s.IsPalindrome());
          
    }
}
}
