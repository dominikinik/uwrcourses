using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;

namespace _4_6
{
    class Program
    {
        static void Main()
        {
            string logFilePath = @"plik.txt";

            
            List<IisLogRecord> logRecords = ReadLogRecords(logFilePath);

            
            var top3Clients = logRecords
                .GroupBy(x => x.ClientIpAddress)
                .Select(x => new { ClientIpAddress = x.Key, RequestCount = x.Count() })
                .OrderByDescending(x => x.RequestCount)
                .Take(3);

            
            Console.WriteLine("Top 3:");
            foreach (var client in top3Clients)
            {
                Console.WriteLine($"{client.ClientIpAddress} {client.RequestCount}");
            }
        }

        static List<IisLogRecord> ReadLogRecords(string logFilePath)
        {
            var logRecords = new List<IisLogRecord>();
            var regexPattern = @"(?<clientIpAddress>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) .*";

            using (var fileStream = new FileStream(logFilePath, FileMode.Open, FileAccess.Read, FileShare.ReadWrite))
            using (var streamReader = new StreamReader(fileStream))
            {
                string line;
                while ((line = streamReader.ReadLine()) != null)
                {
                    Match match = Regex.Match(line, regexPattern);
                    if (match.Success)
                    {
                        string clientIpAddress = match.Groups["clientIpAddress"].Value;
                        logRecords.Add(new IisLogRecord { ClientIpAddress = clientIpAddress });
                    }
                }
            }

            return logRecords;
        }
    }

    class IisLogRecord
    {
        public string ClientIpAddress { get; set; }
    }
}
