'use strict'
var glob = 7
var c = 8;

function printLocal() {
  var a = 123;
  // ha csak c = 9, akkor gáz van
  // ha itt var nelkül irom, hogy d = 10 és nincs use strict-létrehoz egy globális változot
  var c = 9;
  console.log(a);
  console.log(glob);
  console.log('local', c);
}

printLocal();
console.log('kint', c);


//var helyett let és az blockolja vagy functiont használunk
for (var i = 0; i <8; i++) {
  console.log('Hurka');
}

console.log(i);
