'use strict'

function Multyply(number) {
  for (var i=1; i<11; i++) {
    console.log( i + ' * ' + number + ' = ' + i * number);
  }
}

Multyply(2)

function Multyply2(numbers) {
  for (var number = 1; number < numbers + 1; number++) {
    Multyply(number)
  }
}

Multyply2(10)

function Multyply3(number) {
  var output = ''
  for (var i=1; i<11; i++) {
    output += i + ' * ' + number + ' = ' + (i * number) + '\n';
  }
  return output;
}

for (var i = 1; i < 11; i++) {
  console.log(Multyply3(i));
}

function recSzorzo(number) {
  if (i > 10) {
    return '';
  }
  return i + ' * ' + number + ' = ' + (i * number) + '\n' + recSzorzo(number, i + 1);
}

console.log(recSzorzo(4, 1));
