function fiborecu(n) {
  if (n < 2) {
    return n;
  } else {
    return fiborecu(n - 1) + fiborecu(n - 2);
  }
}

function fiboiter(n) {
  var i;
  var a = 0;
  var b = 1;
  var c;
  if (n < 2) {
    return n;
  }
  for (i = 2; i <= n; i++) {
    c = a + b;
    a = b;
    b = c;
  }
  return c;
}
console.log("fiboiter");

for (let i = 0; i < 30; i++) {
  var start = Date.now();
  var wynik = fiboiter(i);
  var koniec = Date.now();

  console.log(wynik, koniec - start);
}
console.log("fiborec");
for (let i = 0; i < 30; i++) {
  var start = Date.now();
  var wynik = fiborecu(i);
  var koniec = Date.now();

  console.log(wynik, koniec - start);
}
