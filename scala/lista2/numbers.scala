import org.w3c.dom.css.Rect
package numbers {
    
    class Rational(n: Int,d: Int = 1 ){
        require(d != 0)
   
        val (num, den) = Rational.reduce(n, d)
        //now operants
        def +(Other: Rational) = 
            new Rational(this.num * Other.den + Other.num * this.den, this.den * Other.den)
        def -(Other: Rational) =
            new Rational(this.num * Other.den - Other.num * this.den, this.den * Other.den)

        def *(Other: Rational) =
            new Rational(this.num * Other.num, this.den * Other.den)
        def /(Other: Rational) =
            new Rational(this.num * Other.den, this.den * Other.num)
        def sqrt: Rational = {
            new Rational(math.sqrt(this.num).toInt, math.sqrt(this.den).toInt)
        }
        def ==(Other: Rational) = 
            this.num == Other.num && this.den == Other.den
        def toDouble: Double = this.num.toDouble / this.den
        override def toString: String = {
            val number = this.num / this.den;
            if (number == 0)
                this.num + "/" + this.den
            else if (this.num % this.den == 0)
                number.toString
            else
                number + " " + this.num % this.den + "/" + this.den
            }
    }
    object Rational {
        def apply(n: Int, d: Int = 1) = new Rational(n, d)
        private def gcd(x: Int, y: Int): Int = 
            if (y == 0) 
                x 
            else 
                gcd(y, x % y)
        def reduce(n: Int, d: Int): (Int, Int) = {
            val g = gcd(n.abs, d.abs)
            if (d < 0 )
                (-n / g, -d / g)
            else
                (n / g, d / g)
            
        }
        
    }

}
package figures{
    import numbers._
    class Point(val x: Rational, val y: Rational) {
       def distance(other: Point): Double = {
           
           val dx = this.x - other.x
           val dy = this.y - other.y
           //
           ((dx * dx) + (dy * dy)).sqrt.toDouble
       }
       
        def isCollinear(p1: Point, p2: Point): Boolean = {
              val a = (this.x - p1.x) * (p2.y - p1.y)
              val b = (p2.x - p1.x) * (this.y - p1.y)
              a == b
         }
        def isOrtagonal(p1: Point, p2: Point): Boolean = {
            val a = ((this.x - p1.x) * (p2.x - p1.x)).toDouble
            val b = ((this.y - p1.y) * (p2.y - p1.y)).toDouble
            a + b == 0
        }
    }

    trait Shape {
        def area: Double
        val desc: String 
}
    class Tringle(val p1: Point, val p2: Point, val p3: Point) extends Shape {
        val desc = "Tringle"
        val a = p1.distance(p2)
        val b = p2.distance(p3)
        val c = p3.distance(p1)
        require(!p1.isCollinear(p2, p3) ||(a + b > c && a + c > b && b + c > a))
        def area: Double = {
            
            val s = (a + b + c) / 2
            math.sqrt(s * (s - a) * (s - b) * (s - c))
        }
    }
    object Tringle {
        def apply(p1: Point, p2: Point, p3: Point) = new Tringle(p1, p2, p3)
    }
    class Rectangle(val p1: Point, val p2: Point) extends Shape {
        val desc = "Rectangle"
        val a = p1.distance(p2)
        val b = p2.distance(p1)
        def area: Double = a * b
    }
    object Rectangle {
        def apply(p1: Point, p2: Point) = new Rectangle(p1, p2)
        def okRectangle(p1: Point, p2: Point, p3: Point, p4: Point): Rectangle = {
            require(isRectangle(p1, p2, p3, p4))
            val a = p1.distance(p2)
            val b = p2.distance(p3)
            val c = p3.distance(p4)
            val d = p4.distance(p1)
            val e = p1.distance(p3)
            val f = p2.distance(p4)
            if (a == c && b == d && e == f)
                new Rectangle(p1, p3)
            else if (a == b && c == d && e == f)
                new Rectangle(p1, p2)
            else if (a == d && b == c && e == f)
                new Rectangle(p1, p4)
            else
                throw new IllegalArgumentException("Not a rectangle")
        }
        private def isRectangle(p1: Point, p2: Point, p3: Point, p4: Point): Boolean = {
           p1.isOrtagonal(p2, p3) &&
           p2.isOrtagonal(p3, p4) &&
            p3.isOrtagonal(p4, p1)
        }    
        def allposible(p1: Point, p2: Point, p3: Point, p4: Point):Boolean = {
            isRectangle(p1, p2, p3, p4) ||
            isRectangle(p2, p3, p1, p4) ||
            isRectangle(p3, p1, p2, p4) }
    }
    class Square(override val p1: Point,override val p2: Point) extends Rectangle(p1, p2){
        override val desc = "Square"
        
        
    }
    object Square {
        def apply(p1: Point, p2: Point) = new Square(p1, p2)
        def okSquare(p1: Point, p2: Point, p3: Point, p4: Point): Square = {
            val a = p1.distance(p2)
            val b = p2.distance(p3)
            val c = p3.distance(p4)
            val d = p4.distance(p1)
            require(Rectangle.allposible(p1, p2, p3, p4)&& a == b && b == c && c == d)
            new Square(p1, p3)
            
        }
    }
}
object Singleton {
    import figures._
    def areaSum(figures: List[Shape]): Double = figures.foldLeft(0.0)((a, b) => a + b.area)
    def printAll(figures: List[Shape]): Unit = figures.foreach(arg => println(arg.desc))
}
object MainApp extends App {
    import figures._
    import numbers._

    val rat1 = new Rational(2, 7)
    val rat2 = new Rational(3, 4)
    val rat3 = new Rational(50, 6)

    val addition = rat1 + rat2
    val subtraction = rat1 - rat2
    val multiplication = rat1 * rat2
    val division = rat1 / rat2

    val p1 = new Point(Rational(1), Rational(1))
    val p2 = new Point(Rational(2), Rational(1))
    val p3 = new Point(Rational(1), Rational(2))
    val p4 = new Point(Rational(1), Rational(3))
    val p5 = new Point(Rational(3), Rational(1))
    val p6 = new Point(Rational(3), Rational(3))

    val tringle = new Tringle(p1, p2, p4)
    val square = new Square(p1, p2)
    val rectangle = new Rectangle(p1, p3)

    val shapes: List[Shape] = List(tringle, square, rectangle)
    println(Singleton.areaSum(shapes))
    Singleton.printAll(shapes)
  }