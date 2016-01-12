'use strict';

var count = 0;

var interval = setInterval(function() {
  count++;
  console.log('Jee-jeee-jee', count);
}, 500);

setTimeout(function() {
  console.log('Booo');
  clearInterval(interval);
}, 5000);
