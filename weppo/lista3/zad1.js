function fib(i) {
  if (i < 3) return 1;
  return fib(i - 1) + fib(i - 2);
}
function fibacc(f) {
  var cache = {};
  return function (n) {
    if (n in cache) {
      return cache[n];
    } else {
      var result = f(n);
      cache[n] = result;
      return result;
    }
  };
}
var fib = fibacc(fib);
console.time();
console.log(fib(6));
console.timeEnd();
console.time();
console.log(fib(50));
console.timeEnd();
console.time();
console.log(fib(12));
console.timeEnd();
