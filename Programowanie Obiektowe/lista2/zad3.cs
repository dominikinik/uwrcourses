//* DOMINIK OLEJARZ
// LISTA 2 PO: ZAD3 

using System;

class BigNum
{
    private int[] digits; // tablica cyfr
    private const int MAX_SIZE = 100; // maksymalny rozmiar tablicy cyfr

    public BigNum(int num)
    {
        digits = new int[MAX_SIZE]; // inicjalizacja tablicy cyfr zerami
        int i = 0;
        while (num > 0)
        {
            digits[i++] = num % 10; // pobieranie kolejnych cyfr z liczby
            num /= 10;
        }
    }

    public void Print()
    {
        bool leadingZeros = true; // flaga określająca, czy przed pierwszą niezerową cyfrą występują zera
        for (int i = MAX_SIZE - 1; i >= 0; i--)
        {
            if (digits[i] != 0)
            {
                leadingZeros = false; // pierwsza niezerowa cyfra została znaleziona, więc nie ma już wiodących zer
            }
            if (!leadingZeros) // jeśli nie ma już wiodących zer, to wypisz cyfrę
            {
                Console.Write(digits[i]);
            }
        }
        if (leadingZeros) // jeśli liczba jest równa zero, to wypisz jedną cyfrę zero
        {
            Console.Write("0");
        }
        Console.WriteLine();
    }

    public static BigNum operator +(BigNum a, BigNum b)
    {
        BigNum result = new BigNum(0);
        int carry = 0; // przeniesienie
        for (int i = 0; i < MAX_SIZE; i++)
        {
            int sum = a.digits[i] + b.digits[i] + carry;
            result.digits[i] = sum % 10; // bieżąca cyfra sumy
            carry = sum / 10; // przeniesienie na kolejną cyfrę
        }
        return result;
    }

    public static BigNum operator -(BigNum a, BigNum b)
    {
        BigNum result = new BigNum(0);
        int borrow = 0; 
        for (int i = 0; i < MAX_SIZE; i++)
        {
            int diff = a.digits[i] - b.digits[i] - borrow;
            if (diff < 0)
            {
                diff += 10; // pożyczka z poprzedniej cyfry
                borrow = 1;
            }
            else
            {
                borrow = 0;
            }
            result.digits[i] = diff;
        }
        return result;
    }
}
BigNum a = new BigNum(123456789);
BigNum b = new BigNum(987654321);
BigNum c = a + b;
BigNum d = b - a;
a.Print(); 
b.Print(); 
c.Print(); 
d.Print(); 
