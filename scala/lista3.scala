object HandleException {
  def unSafe[T](ex: Exception)(block: => T) = try {
    block
  } catch {
    case e: Throwable => {
      println(s"Exception occured: ${e.getMessage()}")
      throw ex;
    }
  }
}
object Utils {
def isSorted(as: List[Int], ordering: (Int, Int) => Boolean) =
    as.zip(as.tail).forall((x, y) => ordering(x, y))

def isAscSorted(as: List[Int]) = 
    isSorted(as, (x: Int, y: Int) => x <= y)


def isDescSorted(as: List[Int]) = 
    isSorted(as, (x: Int, y: Int) => x >= y)
//A typ B acumulator 
def foldLeft[A, B](l: List[A], z: B)(f: (B, A) => B): B = 
    def foo (xs: List[A], acc: B, f: (B, A) => B): B = 
        if (xs == Nil) acc
        else foo(xs.tail, f(acc, xs.head), f)
    foo(l, z, f) 
       
def sum(l: List[Int]) = 
    foldLeft(l, 0)((x, y) => x + y)
def length[A](l: List[A]) =
    foldLeft(l,0)((x, y) => x + 1)
def compose[A, B, C](f: B => C, g: A => B ) =(x : A) => f(g(x))

def repeated[A](f: A => A, n: Int): A => A = 
    if (n <= 0) (x: A) => x
    else compose(f, repeated(f, n-1))


def curry[A, B, C](f: (A, B) => C): A => B => C = 
        a => b => f(a, b)
def uncurry[A, B, C](f: A => B => C): (A, B) => C = 
        (a, b) => f(a)(b)
}
object Main extends App {
  val sortedAscending = List(1, 2, 3, 4)
  val sortedAscending2 = List(1, 1, 3, 4, 5, 5)
  val sortedDescending = List(10, 8, 7, 7, 7, 6, 3, 0,-1)
  require(Utils.isSorted(sortedAscending, (a: Int, b: Int) => a < b))
  require(!Utils.isSorted(sortedAscending2, (a: Int, b: Int) => a < b))
  require(Utils.isAscSorted(sortedAscending2))  
  require(Utils.isDescSorted(sortedDescending))

  require(Utils.sum(sortedAscending) == 10)
  require(Utils.length(sortedAscending) == 4)

  require(Utils.compose((x: Int) => x + 1, (x: Int) => x * x)(2) == 5)
  require(Utils.repeated((x: Int) => x + 1, 3)(0) == 3)

  val add = (a: Int, b: Int) => a + b
  val addCurried = Utils.curry(add)
  require(addCurried(1)(1) == 2)
  require(Utils.uncurry(addCurried)(1, 1) == 2)

  HandleException.unSafe(new Exception("Test")) {
   println(10 / 0)
   println(Utils.repeated((x: Int) => x * x, 0)(1))
  }
}