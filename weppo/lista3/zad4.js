function sum(...z) {
    var acc=0
    for (b of z)
    {
        acc=acc+b
    }
    return acc
    }

    console.log(sum(1,2,3));
    // 6
    console.log(sum(1,2,3,4,5));
    // 15
    