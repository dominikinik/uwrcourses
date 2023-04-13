let boomcykcyk = {
  x: 3,

  get fun() {
    return boomcykcyk.n;
  },

  set fun(n) {
    boomcykcyk.n = n + 7;
  },

  metoda: function () {
    console.log(boomcykcyk.n);
  },
};

//  pola i metody można dodawać wszystkim
boomcykcyk["q"] = 12;
console.log(boomcykcyk["q"]);

boomcykcyk.jakas = function () {
  return boomcykcyk.x * boomcykcyk.q;
};
console.log(boomcykcyk.jakas());

// get/set  tylko   defineProperty

Object.defineProperty(boomcykcyk, "byqu", {
  get: function () {
    return boomcykcyk.x;
  },

  set: function (i) {
    boomcykcyk.x = i + 10;
  },
});

boomcykcyk.byqu = 35;
console.log(boomcykcyk.byqu);
