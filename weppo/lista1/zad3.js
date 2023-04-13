function isPrime(num) {
  var prime = true;
  for (var i = 2; i * i <= num; i++) {
    if (num % i == 0) {
      prime = false;
      break;
    }
  }
  return prime;
}
for (let i = 2; i <= 100000; i++) {
  if (isPrime(i) == true) console.log(i);
}
