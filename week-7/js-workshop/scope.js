'use strict'

var g = 123;

function printG() {
  console.log(g);
  g = 323
}

printG();
console.log(g);

function printLocalG() {
  var g = 7;
  console.log(g);
}

printLocalG();
console.log(g);

/*function printA() {
  var a = 123;
  console.log(a);
}

printA();
console.log(a);*/

if (true) {
  let c = 999;
  console.log(c)
}
