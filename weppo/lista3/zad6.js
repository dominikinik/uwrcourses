function fib1() {
    [a, b] = [0, 1]
    return {
        next: function () {
            let fib = a;
            [a, b] = [b, a + b];
            return {
                value: fib,
                done: false
            }
        }
    }
}

function* fib2() {
    var [a, b] = [0, 1]
    while (true) {
        yield a;
        [a, b] = [b, a + b]
    }
}

/*
var _it = fib1();
for ( var _result; _result = _it.next(), !_result.done; ) {
console.log( _result.value );
}dziala*/
/*
    for ( var i of fib2() ) {
        console.log( i );
        }dziala*/
/*iteratory sa nie reuzywalne przez to nie da sie po nich w ten sposob iterowac
for (var i of fib1()){
console.log(i)
}nee*/