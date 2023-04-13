const sql = require("mssql");

async function getdata() {
  var conn = new sql.ConnectionPool({
    server: 'localhost',
    port: 1433,
    database: 'Zadania',
    user: 'fee',
    password: 'fee',
    encrypt: false
  });
  try {
    await conn.connect();
    var request= new sql.Request(conn);
    var result = await request.query("select * from OSOBA");
    result.recordset.forEach((r)=> 
    {console.log(`${r.ID} ${r.IMIE}`)});
    await conn.close();
  }
   catch (err) {
    if (conn.connected) conn.close();
    console.log(err);
  }
}




const config = {
  server: 'localhost',
    port: 1433,
    database: 'Zadania',
    user: 'fee',
    password: 'fee',
    encrypt: false
};

async function insertIntoOSOBA() {
  try {
    const pool = await sql.connect(config);

    const result = await pool.request()
      .query`DECLARE @next_id INT
             SELECT @next_id = NEXT VALUE FOR OSOBA_SEQ

             INSERT INTO OSOBA (ID, IMIE, NAZWISKO, PLEC)
             OUTPUT INSERTED.ID
             VALUES (@next_id, 'Janek2312331', 'Kowalski12', 'M')`;

    console.log(`nowe id' ID: ${result.recordset[0].ID} wstawione`);
  } catch (err) {
    console.log(err);
  } finally {
    sql.close();
  }
}

async function insertIntoOSOBA2() {
  try {
    const pool = await sql.connect(config);

    const result = await pool.request()
      .query`INSERT INTO OSOBA2 (IMIE, NAZWISKO, PLEC)
             OUTPUT INSERTED.ID
             VALUES ('Jan', 'Kowalski', 'M')`;

    console.log(`nowe ID: ${result.recordset[0].ID} wstawione`);
  } catch (err) {
    console.log(err);
  } finally {
    sql.close();
  }
}
getdata()
insertIntoOSOBA2();
insertIntoOSOBA();
getdata()