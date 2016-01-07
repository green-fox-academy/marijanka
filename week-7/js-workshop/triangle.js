'use strict';

function triangle(number) {
  if (number >= 1) {
    var max_size = 1 + (number - 1) * 2;
    for (var i = 1; i < number * 2; i += 2) {
      console.log(' '.repeat((max_size-i)/2) + '*'.repeat(i));
    }
  }
}

triangle(8)
/*
  *
 ***
*****
*/
