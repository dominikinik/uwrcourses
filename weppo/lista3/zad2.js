function forEach(a, f) {
  for (var b of a) {
    f(b);
  }
}
function map(a, f) {
  var odp2 = [];
  for (var b of a) {
    odp2.push(f(b));
  }
  return odp2;
}
function filter(a, f) {
  var odp = [];
  for (var b of a) {
    if (f(b)) odp.push(b);
  }
  return odp;
}
var a = [1, 2, 3, 4];
forEach(a, (_) => {
  console.log(_);
});
// [1,2,3,4]
console.log(filter(a, (_) => _ < 3));

// [1,2]
console.log(map(a, (_) => _ * 2));
// [2,4,6,8]
