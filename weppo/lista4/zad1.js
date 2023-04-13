function Tree(val, left, right) {
    this.left = left;
    this.right = right;
    this.val = val;
}
Tree.prototype[Symbol.iterator] = function* () {
    let q = []
    q.push(this)

    while (q) {
        let curr = q.shift();
        if (curr == undefined)
            break;
        if (curr.right)
            q.push(curr.right)
        if (curr.left)
            q.push(curr.left)
        yield curr.val;
    }
}


var root = new Tree(1,
    new Tree(2
        , new Tree(3, new Tree(5), new Tree(6))),
    new Tree(4));
for (var e of root) {
    console.log(e);
}
