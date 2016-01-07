'use strict';

// use strict nélkül működik:
/*var student = {
  age: 10,
  sayYourAge: sayYourAge
};

function sayYourAge() {
  console.log('I am ' + this.age);
}

age = 12;

student.sayYourAge();

sayYourAge();
*/

var student = {
  age: 10,
  sayYourAge: sayYourAge
};

function sayYourAge() {
  console.log('I am ' + this.age);
}

var func = student.sayYourAge();
func();
