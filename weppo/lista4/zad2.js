var Foo = (function() {
    function Bar() {
        Qux();
        console.log("Qux z metody bar");
    }

    function Qux() {
        console.log("Qux z siebie");
    }

    function Foo() {}

    
    Foo.prototype.Bar = Bar;   
    // Foo.prototype.Qux = Qux; 

    return Foo;
}());


var foo = new Foo(); 
console.log(Object.getPrototypeOf(foo));
//console.log(Object.getPrototypeOf(foo.Qux)); // błąd
foo.Bar();