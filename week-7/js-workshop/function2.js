'use strict'

function greet(name) {
  console.log('Csaaa ' + name + '!');
}

greet('Mariann');

var koszontes = greet;

koszontes('Gyuri');

var print = console.log;

function greeter(name, log) {
  log("Csovi " + name + '!');
}

greeter('Lajoskam', print);

function add(a, b) {
  return a+b
}

console.log(add(1, 3));

var add2 = function (a, b) {return a + b; };
console.log(add2(1, 3));

function customLogger (text) {
  console.log(text, "logged by my function");
}

greeter('Csabi', customLogger);
