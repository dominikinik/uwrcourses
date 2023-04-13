// Operator "instanceof" działa jak predykat,sprawdz czy dana wartosc pochodzi z konstrunktora danego typu
console.log(new String("lolxd") instanceof String);
var Foobar = null;
var o = {};
Object.setPrototypeOf(o, Foobar);
console.log(o instanceof Object);
console.log("beka" instanceof String);

console.log(new Number(121212) instanceof Number);

//zwraca napis jakiego typu jest zmienna
console.log(typeof "erwr");
console.log(typeof new String("werw"));
console.log(typeof 131231);
console.log(typeof new Number(1231231));
