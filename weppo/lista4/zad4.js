

process.stdout.write("Witaj, podaj swoje imię: ")

process.stdin.on('data', data => {
    console.log('Wprowadziles dane: '+ data  );
    process.exit();
  });