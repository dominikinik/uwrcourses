function fib(i) {

  if (i < 2)
      return 1
  return fib(i - 1) + fib(i - 2)
}
console.time();
console.log(fib(6))
console.timeEnd();
console.time();
console.log(fib(50))
console.timeEnd();
console.time();
console.log(fib(12))
console.timeEnd();