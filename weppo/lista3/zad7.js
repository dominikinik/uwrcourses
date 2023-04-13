function* gorne(it, top) {
    for (let i = 0; i < top; i++) {
        let next = it.next();
            yield next.value
        }
    }
    function* fib() {
        var [a, b] = [0, 1]
        while (true) {
            yield a; 
            [a, b] = [b, a + b]
        }
    }
    
    for (let num of gorne( fib(), 6) ) {
    console.log(num);
    }
    