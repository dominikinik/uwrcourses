var fs = require('fs');
var https = require('https');
(async function () {
 var pfx = await fs.promises.readFile('test21.pfx');
 var server = https.createServer({
 pfx: pfx,
 passphrase: '123'
 },
 (req, res) => {
 res.setHeader('Content-type', 'text/html; charset=utf-8');
 res.end(`hello world ${new Date()}`);
 });
 server.listen(2000);
 console.log('started');
})(); 