'use strict';

function Student() {
  this.objects = {};
  this.addGrade = function(subject, grade) {
    if (!(subject in this.objects)) {
      this.objects[subject] = [];
    }
    this.objects[subject].push(grade);
  }
  this.getCount = function() {
    var output = {};
    for (var key in this.objects) {
      output[key] = this.objects[key].length;
    }
    return output;
  }
  this.getAverageBySubject = function() {
    var output = {};
    for (var key in this.objects) {
      var sum = this.objects[key].reduce(function(acc, num) {
        return acc + num;
      }, 0);
      output[key] = sum / this.objects[key].length;
    }
    return output;
  }
  this.getAverage = function() {
    var avarage = this.getAverageBySubject();
    var sum = 0;
    var grade_number = 0;
    for (var key in avarage) {
      sum += avarage[key];
      grade_number += 1;
    }
    return sum / grade_number;
  }
  this.getAverage_stupid = function() {
    var sum = 0;
    var count = 0;
    for (var key in this.objects) {
      this.objects[key].forEach(function(grade) {
        sum += grade;
        count += 1;
      });
      return sum / count;
    }
  }
}

var dezso = new Student();
dezso.addGrade('matek', 5);
dezso.addGrade('matek', 4);
dezso.addGrade('matek', 4);
dezso.addGrade('rajz', 1);
dezso.addGrade('rajz', 3);

console.log(dezso.objects);
console.log(dezso.getCount()); // ('rajz': 2; matek:3)
console.log(dezso.getAverage()); //3.4
console.log(dezso.getAverageBySubject());

//szorgalmi
// // ('matek': 4.3, 'rajz': 2)

//var obj = {}, obj['x'] = [1, 3, 4], obj['x'].push(5)
