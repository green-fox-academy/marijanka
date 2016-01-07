'use strict'

function summa(list) {
  var sum = 0;
  for (var i = 0; i < list.length; i++) {
    sum += list[i];
  }
  return sum;
}

function summa2(list) {
  for (var i = 0, sum = 0; i < list.length; sum += list[i++]);
  return sum;
}

console.log(summa([1, 2, 3, 4, 5, 6]));
console.log(summa([2, 3, 5]));
console.log(summa2([2, 3, 5]));
