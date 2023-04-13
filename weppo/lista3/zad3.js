function createFs(n) {
  var fs = [];
  for (var i = 0; i < n; i++) {
    fs[i] = (function (j) {
      return function () {
        return j;
      };
    })(i);
  }
  return fs;
}
// var wiazanie w obrebie funkcji a nie bloku
// let nowa za kazdym razem petli
// funkcje w tablicy maja  referencję na tę samą zmienną i a ta ma 10 numer
var myfs = createFs(10);
console.log(myfs[0]());
console.log(myfs[2]());
console.log(myfs[7]());
