const fs = require('fs');

function read(path, encoding) {
    return fs.readFile(path, encoding, (err, data) => {
        if (err) {
            console.error(err);
            return;
        }
        console.log(data);
    })
};

read('xsx.txt', 'utf-8');