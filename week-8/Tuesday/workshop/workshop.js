'use strict';

var isEnd =false;
setTimeout(function() {
  console.log('JEJ');
  isEnd = true;
}, 1000);


function end(){
  console.log('End');
  console.log('End2');
}

end();

while (!isEnd) {}
