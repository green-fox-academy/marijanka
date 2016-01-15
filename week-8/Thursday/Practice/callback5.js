'use strict';

var fs = require('fs');

function countLetterPInAlmaTxt(callback) {
  fs.readFile('alma.txt', function(err, content) {
    var count = 0;
    var stringContent = String(content);
    for (var letter = 0; letter < stringContent.length; letter++) {
      if (stringContent[letter] === 'p') {
        count ++;
      }
    }
    callback(count);
  });
}

countLetterPInAlmaTxt(function (count) {
  console.log(count);
});
