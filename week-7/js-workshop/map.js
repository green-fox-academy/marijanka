'use strict'

var benaszavak = [
  'kuty',
  'macsk',
  'alm',
];

var faszaszavak = [];

for (var i = 0; i < benaszavak.length; i++) {
  faszaszavak.push(benaszavak[i] + 'a');
}

console.log(faszaszavak);

var faszaszavak2 = [];

benaszavak.forEach(function(szo) {
  faszaszavak2.push(szo + 'a');
});

console.log(faszaszavak2);

var faszaszavak3 = benaszavak.map(function(szo) {
  return szo + 'a';
});

console.log(faszaszavak3);

//Szorzotabla

var szorzotabla1 = '';

for (var i =1; i < 11; i++) {
  szorzotabla1 += i + ' * ' + 4 + ' = ' + i * 4 + '\n';
}
console.log(szorzotabla1);

var szorzotabla2 = '';
var szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

szamok.forEach(function(e) {
  szorzotabla2 += e + ' * ' + 4 + ' = ' + e * 4 + '\n';
});
console.log(szorzotabla2);

var szorzotabla3 = '';
var sorok = szamok.map(function(e) {
  return e + ' * ' + 4 + ' = ' + e * 4;
})

szorzotabla3 = sorok.join('\n');
console.log(szorzotabla3);
