for (let i = 1; i <= 100000; i++) {
  var sum = 0;
  flag = 0;
  for (let j = 0; j < i.toString().length; j++) {
    sum = sum + +i.toString().charAt(j);
    if (i % i.toString().charAt(j) != 0) {
      flag = 1;
      break;
    } else flag = 0;
  }
  if (i % sum == 0 && flag == 0) console.log(i, sum);
}
