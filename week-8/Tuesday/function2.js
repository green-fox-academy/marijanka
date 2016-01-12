'use strict';

var human = {
  word : ['kacsa', 'macska', 'MAmmlasz'],
  name : 'Tibor',
  speak : speak,
  say : say
};

function speak () {
  var _this = this;
  this.word.forEach(function(w){
    console.log('I am ' + _this.name);
    console.log('Bla-bla-bla' + w);
  });
}

function say(w) {
  console.log('I am ' + _this.name);
  console.log('Bla-bla-bla' + w);
}


human.speak();
