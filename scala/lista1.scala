def scalarUgly(xsInit: List[Int], ysInit: List[Int]): Int = {
    require(xsInit.size == ysInit.size && xsInit.size > 0)
    var sum = 0
    var xs = xsInit
    var ys = ysInit
    while {
        sum += xs.head * ys.head;
        xs = xs.tail
        ys = ys.tail
        xs != Nil
    } do ()
    sum
}
def scalar(xs: List[Int], ys: List[Int]): Int = {
    require(xs.size == ys.size && xs.size > 0)
    (for {(x, y) <- xs zip ys} yield x * y).sum
    }
    
def sortUgly(xs: List[Int]): List[Int] = {
    if (xs == Nil) {
      xs
    } else {
         
      var i = 1
      var pivot = xs.head
      var listSmallerOrEqual = List[Int]()
      var listBigger = List[Int]()
      while {
      if (i < xs.size) {
        if (xs(i) < pivot) {
          listSmallerOrEqual = xs(i) +: listSmallerOrEqual
        } else {
          listBigger = listBigger :+ xs(i)
        }
        i += 1
      }
      i < xs.size
    } do ()

      sortUgly(listSmallerOrEqual) ::: (pivot +: sortUgly(listBigger))
    }
  }
def sort(xs: List[Int]): List[Int] = {
    if (xs == Nil) {
      xs
    } else {
      val pivot = xs.head
      val listSmallerOrEqual = for (x <- xs.tail if x <= pivot) yield x
      val listBigger = for (x <- xs.tail if x > pivot) yield x
      sort(listSmallerOrEqual) ::: (pivot +: sort(listBigger))
    }
  }
def isPrimeUgly(n: Int): Boolean = {
    var i=2
    if (n <= 1) {
    false
    } else {
        while  {
            if (n % i == 0) {
                return false
            }
            i += 1
            i <= math.sqrt(n).ceil.toInt
            
        }do ()
        true}}

def isPrime(n: Int): Boolean = {
if (n <= 1) {
    false
} else {
    val limit = math.sqrt(n).ceil.toInt 
    (for (i <- 2 to limit if n % i == 0) yield i) == Nil
    
}
}
def primePairsUgly(n : Int): List[(Int, Int)]= {
    var i = 1
    var resultList = List[(Int, Int)]()
    while  {
      var j = i + 1
      while  {
        if (isPrime(i + j)) {
          resultList = (i, j) +: resultList
        }
        j += 1
        j < n
      } do ()
      i += 1
      i < n
    } do ()
    resultList.reverse
  }
def primePairs(n : Int): List[(Int, Int)] = 
    (for {
        i <- 1 until n
        j <- i + 1 until n
        if isPrime(i + j)
    } yield (i, j)).toList
val filesHere = new java.io.File(".").listFiles
def fileLinesUgly(file: java.io.File): List[String] = {
    var lines = List[String]()
    val reader = new java.io.BufferedReader(new java.io.FileReader(file))
    var line = reader.readLine()
    while  {
        lines = line :: lines
        line = reader.readLine()
        line != null
    }do ()
    lines.reverse
     
}
def fileLines(file: java.io.File): List[String] = {
    scala.io.Source.fromFile(file, "ISO-8859-1").getLines.toList
  }
//jesli for jest wymuszany 
/*
def fileLines(file: java.io.File): List[String] = {
    val reader = new java.io.BufferedReader(new java.io.FileReader(file))
    
    (for {
        line <- Iterator.continually(reader.readLine()).takeWhile(_ != null)
    } yield line).toList
}
 */
def printNonEmptyUgly(pattern: String): Unit = {
    require(new java.io.File(pattern).isDirectory)
    var filesHere = new java.io.File(pattern).listFiles
    var len = filesHere.length
    var i = 0
    while (i < len) {
      var file = filesHere(i)
      if (file.length != 0 && file.toString.split("\\.").last == "scala") {
        println(file.toString)
      }
      i += 1
    }
  }
def printNonEmpty(pattern: String): Unit = {
    require(new java.io.File(pattern).isDirectory)
    val filesHere = new java.io.File(pattern).listFiles
    filesHere.filter(f => f.length != 0 && f.toString.split("\\.").last == "scala").foreach(f => println(f.toString))
  }

object Main {
  def main(args: Array[String]): Unit = {
    val result = scalarUgly(List(1, 2, 3), List(4, 5, 6))
    val result2 = scalar(List(1, 2, 3), List(4, 5, 6))
    val result3 = sortUgly(List(3, 2, 1))
    val result4 = sort(List(3, 2, 1))
    val result5 = isPrimeUgly(7)
    val result6 = isPrime(7)
    val result7 = primePairsUgly(10)
    val result8 = primePairs(10)
    val result9 = fileLinesUgly(new java.io.File("cos.txt"))
    val result10 = fileLines(new java.io.File("cos.txt"))
    printNonEmptyUgly(".")
    printNonEmpty(".")

    println(result)
    println(result2)
    println(result3)
    println(result4)
    println(result5)
    println(result6)
    println(result7)
    println(result8)
    println(result9)
    println(result10)
    

  }
}
