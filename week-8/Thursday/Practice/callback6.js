'use stict';

var fs = require('fs');

function countLetterInAlmaTxt(almaLetter, callback) {
  fs.readFile('alma.txt', function(err, content) {
    var count = 0;
    var stringContent = String(content);
    for (var letter = 0; letter < stringContent.length; letter++) {
      if (stringContent[letter] === almaLetter) {
        count ++;
      }
    }
    callback(count);
  });
}


countLetterInAlmaTxt('a', function(count) {
  console.log(count);
});
