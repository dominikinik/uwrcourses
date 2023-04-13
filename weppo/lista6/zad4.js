const express = require('express');
const app = express();
const bodyParser = require('body-parser');

// użycie body-parser do przetwarzania danych z formularza
app.use(bodyParser.urlencoded({ extended: true }));

// widok formularza zgłoszenia
app.get('/', (req, res) => {
    res.send(`
        <form action="/print" method="post">
            Imię: <input type="text" name="firstName"><br>
            Nazwisko: <input type="text" name="lastName"><br>
            Nazwa zajęć: <input type="text" name="className"><br><br>

            <h4>Deklarowane zadania:</h4>
            <table>
                <tr>
                    <th>Zadanie</th>
                    <th>Liczba punktów</th>
                </tr>
                <tr>
                    <td>Zadanie 1</td>
                    <td><input type="number" name="task1"></td>
                </tr>
                <tr>
                    <td>Zadanie 2</td>
                    <td><input type="number" name="task2"></td>
                </tr>
                <tr>
                    <td>Zadanie 3</td>
                    <td><input type="number" name="task3"></td>
                </tr>
              
            </table>
            <input type="submit" value="Wyślij">
        </form>
    `);
});

// widok wydruku
app.post('/print', (req, res) => {
    let firstName = req.body.firstName;
    let lastName = req.body.lastName;
    let className = req.body.className;

    if (!firstName || !lastName || !className) {
        res.send('Proszę uzupełnić wszystkie pola');
        return;
    }

    let taskPoints = [];
    for (let i = 1; i <= 10; i++) {
        taskPoints.push(req.body[`task${i}`] || 0);
    }

    res.send(`
        <h2>Pasek zgłoszenia zadań</h2>
        <p>Imię i nazwisko: ${firstName} ${lastName}</p>
        <p>Nazwa zajęć: ${className}</p>
        <p>Wyniki zadań: ${taskPoints.join(', ')}</p>
        <button onclick="window.print()">Drukuj</button>
    `);
});

app.listen(5000, () => {
    console.log('Aplikacja uruchomiona na porcie 5000');
});