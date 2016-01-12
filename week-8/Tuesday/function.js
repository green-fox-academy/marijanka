'use strict';

var button = document.queryselector('button');

button.addEvenListener ('click', function () {
  shout('kacsa');
});

function shout(word) {
  console.log('AJAJJAJA');
  console.log('AJAJJAJA');
  console.log('AJAJJAJA', word);
  console.log('AJAJJAJA');
  console.log('AJAJJAJA');
}
