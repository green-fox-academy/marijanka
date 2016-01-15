'use strict';

var fs = require('fs');

function readAlmaTXT(callback) {
  fs.readFile('alma.txt', function(err, content) {
    var output = String(content);
    callback(output);
  });
}

readAlmaTXT(function(content) {
  console.log(content);
});
