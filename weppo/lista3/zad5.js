function createGenerator(x) {
    return function () {
        var _state = 0;
        return {
            next: function () {
                return {
                    value: _state,
                    done:  _state++ >= x
                }
            }
        }
    }
}

var ob1 = {
    [Symbol.iterator]: createGenerator(10)
};

var ob2 = {
    [Symbol.iterator]: createGenerator(22)
}

var ob3 = {
    [Symbol.iterator]: createGenerator(33)
}

for (var f of ob1) {
    console.log(f);
}
console.log("--------------")
for (var f of ob2) {
    console.log(f);
}
console.log("--------------")

for (var f of ob3) {
    console.log(f);
}