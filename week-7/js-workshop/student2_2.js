'use strict';

function Student() {
  this.objects = [];
  this.addGrade = function(s, g) {
    this.objects.push({subject: s, num: g});
  };

  this.getCount = function() {
    var output = {};
    this.grades.forEach(function(grade) {
      if (!(grade.subject in output)) {
        output[grade.subject] = 0;
      }
      output[grade.subject]++;
    });
    return output;
  }
  this.getAverage = function() {
    var sum = 0;
    this.grades.forEach(function(grade) {
      sum += grade[num];
    });
    return sum / this.grades.length;
  };
