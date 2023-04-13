using System;

class Program
{
    static void Main(string[] args)
    {
        for (int i = 1; i <= 100000; i++)
        {
            bool divisibleByDigits = true;
            int digitSum = 0;
            int n = i;
            while (n > 0)
            {
                int digit = n % 10;
                if (digit == 0 || i % digit != 0)
                {
                    divisibleByDigits = false;
                    break;
                }
                digitSum += digit;
                n /= 10;
            }
            if (divisibleByDigits && i % digitSum == 0)
            {
                Console.WriteLine(i);
               
            }
        }
    }
}
