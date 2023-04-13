using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace zdadanie2._7
{
    public class Vector2D
    {
        public double X { get; set; }
        public double Y { get; set; }

        public Vector2D(double x, double y)
        {
            X = x;
            Y = y;
        }

        public static Vector2D operator +(Vector2D v1, Vector2D v2)
        {
            return new Vector2D(v1.X + v2.X, v1.Y + v2.Y);
        }

        public static Vector2D operator -(Vector2D v1, Vector2D v2)
        {
            return new Vector2D(v1.X - v2.X, v1.Y - v2.Y);
        }

        public static Vector2D operator *(Vector2D v, double scalar)
        {
            return new Vector2D(v.X * scalar, v.Y * scalar);
        }

        public static Vector2D operator /(Vector2D v, double scalar)
        {
            if (scalar == 0) throw new DivideByZeroException();
            return new Vector2D(v.X / scalar, v.Y / scalar);
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Vector2D v1 = new Vector2D(1, 2);
            Vector2D v2 = new Vector2D(3, 4);
            Vector2D v3 = v1 + v2; // v3 = (4, 6)
            Vector2D v4 = v3 * 2; // v4 = (8, 12)
            Vector2D v5 = v4 / 2; // v5 = (4, 6)
            Vector2D v6 = v5 - v1; // v6 = (3, 4)

        }
    }
}
