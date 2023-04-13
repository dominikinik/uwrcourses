using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _4_4
{
    internal class Program
    {
        static void Main(string[] args)
        {

            string folderPath = @"C:\Users\dominik\Desktop\lista6";
            long totalLength = Directory.GetFiles(folderPath)
                .Select(file => new FileInfo(file).Length)
                .Aggregate((length1, length2) => length1 + length2);

            Console.WriteLine(totalLength);
        }
    }
}
