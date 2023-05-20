using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ClassLibrary1
{

    public class Wektor
    {
        public float[] wspolrzedne; // tablica przechowująca współrzędne
        public int wymiar; // wymiar wektora

        public Wektor(int wymiar)
        {
            this.wymiar = wymiar;
            wspolrzedne = new float[wymiar];
        }

        public float Norma()
        {
            float sumaKwadratow = 0;

            for (int i = 0; i < wymiar; i++)
            {
                sumaKwadratow += wspolrzedne[i] * wspolrzedne[i];
            }

            return (float)Math.Sqrt(sumaKwadratow);
        }

        public static Wektor operator +(Wektor v1, Wektor v2)
        {
            if (v1.wymiar != v2.wymiar)
            {
                throw new ArgumentException("Wektory muszą mieć ten sam wymiar.");
            }

            Wektor wynik = new Wektor(v1.wymiar);

            for (int i = 0; i < v1.wymiar; i++)
            {
                wynik.wspolrzedne[i] = v1.wspolrzedne[i] + v2.wspolrzedne[i];
            }

            return wynik;
        }

        public static float operator *(Wektor v1, Wektor v2)
        {
            if (v1.wymiar != v2.wymiar)
            {
                throw new ArgumentException("Wektory muszą mieć ten sam wymiar.");
            }

            float iloczyn = 0;

            for (int i = 0; i < v1.wymiar; i++)
            {
                iloczyn += v1.wspolrzedne[i] * v2.wspolrzedne[i];
            }

            return iloczyn;
        }

        public static Wektor operator *(float skalar, Wektor v)
        {
            Wektor wynik = new Wektor(v.wymiar);

            for (int i = 0; i < v.wymiar; i++)
            {
                wynik.wspolrzedne[i] = skalar * v.wspolrzedne[i];
            }

            return wynik;
        }
    }
}
