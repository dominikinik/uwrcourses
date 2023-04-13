//* DOMINIK OLEJARZ
// LISTA 2 PO: ZAD4 
using System;
using System.Collections.Generic;

class LazyIntList
{
    private List<int> elements;

    public LazyIntList()
    {
        elements = new List<int>();
    }

    public int element(int i)
    {
        if (i >= elements.Count)
        {
            for (int j = elements.Count; j <= i; j++)
            {
                elements.Add(j);
            }
        }
        return elements[i];
    }

    public int size()
    {
        return elements.Count;
    }
}

class LazyPrimeList : LazyIntList
{
    private List<int> primes;

    public LazyPrimeList() : base()
    {
        primes = new List<int>();
    }

    private bool isPrime(int n)
    {
        if (n < 2)
        {
            return false;
        }
        for (int i = 2; i <= Math.Sqrt(n); i++)
        {
            if (n % i == 0)
            {
                return false;
            }
        }
        return true;
    }

    public new int element(int i)
    {
        if (i >= primes.Count)
        {
            for (int j = primes.Count; j <= i; j++)
            {
                int n = elements[j];
                while (!isPrime(n))
                {
                    n++;
                }
                primes.Add(n);
            }
        }
        return primes[i];
    }
}
LazyPrimeList primes = new LazyPrimeList();
Console.WriteLine(primes.size()); 
Console.WriteLine(primes.element(0)); 
Console.WriteLine(primes.size()); 
Console.WriteLine(primes.element(10)); 
Console.WriteLine(primes.size()); 
