let a = {};

a.b = 112;
console.log(a["b"]);

a["c"] = 12;
console.log(a.c);

// Jakie są różnice między tymi dwoma sposobami?

a["h y e"] = [];

// console.log(a.h y e)

// Co się dzieje jeśli argumentem operatora jest liczba?

let b = {};
b[1] = 1;
console.log(b);
b["1"] = 2;
console.log(b);

// Co się dzieje jeśli argumentem operatora jest inny obiekt?

b[a] = 2;
console.log(b);

b[{}] = 3;
console.log(b);

b["[object Object]"] = {};
console.log(b);

// Jaki wpływ na klucz pod jakim zapisana zostanie wartość ma programista w obu przypadkach?
// gdy obiekt metoda tostring
// W przypadku liczb liczba zamieniana wewnetrznie na znaki bez wplywu

// Co się dzieje jeśli argumentem operatora jest napis?
console.log("__________________________________________________");
let tab = [1, 2, 3, 4];
let x = {
  beka: null,
  toString: () => "5",
};
tab[x] = 8;
console.log("____");
console.log(tab);
console.log(tab.length);
console.log(tab["3"]); // nappis =>liczba jesli sie da

tab["0"] = "0";
console.log(tab);

tab["a"] = "b";
// Klucz jest dodawany  obiektu.
console.log(tab);
console.log(tab.length); // ale długość tablicy sie nie zmienia

// Co się dzieje jeśli argumentem operatora jest inny obiekt?

tab[{}] = {};
console.log(tab); // obiekty w tabliach zachowuja sie identycznie jak w obiektach

console.log("__________________________________________________________");
tab.length = 1;
console.log(tab);

tab.length = 20;
console.log(tab);
