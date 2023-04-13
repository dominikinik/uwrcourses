const sql = require("mssql");


const config = {
    server: 'localhost',
      port: 1433,
      database: 'Zadania',
      user: 'fee',
      password: 'fee',
      encrypt: false
  };

async function updateOSOBA(id, imie, nazwisko, plec) {
    try {
      const pool = await sql.connect(config);
  
      await pool.request()
        .input('id', sql.Int, id)
        .input('imie', sql.VarChar(255), imie)
        .input('nazwisko', sql.VarChar(255), nazwisko)
        .input('plec', sql.Char(1), plec)
        .query`UPDATE OSOBA
               SET IMIE = @imie, NAZWISKO = @nazwisko, PLEC = @plec
               WHERE ID = @id`;
  
      console.log(`zmienione ID: ${id}`);
    } catch (err) {
      console.log(err);
    } finally {
      sql.close();
    }
  }
  async function deleteOSOBA(id) {
    try {
      const pool = await sql.connect(config);
  
      await pool.request()
        .input('id', sql.Int, id)
        .query`DELETE FROM OSOBA
               WHERE ID = @id`;
  
      console.log(`usuniete ID: ${id} `);
    } catch (err) {
      console.log(err);
    } finally {
      sql.close();
    }
  }
  updateOSOBA(1,"Jan","Kowalski","M")
  deleteOSOBA(2)