'use strict';

var kids = [
  {name: 'Tibor', candies:2},
  {name: 'Jozsi', candies:3},
  {name: 'Agoston', candies:0},
  {name: 'Julika', candies:7},
  {name: 'Steve', candies:4}
]


function getTheRichestKidsName2(kids) {
  var richestKid = kids[0];
  for (var i = 1; i = kids.length; i++) {
    if (kids[i].candies > richestKid) {
      richestKid = currentKid;
    }
  }
  return richestKid.name;
}

console.log(getTheRichestKidsName2(kids));
/*
function theMostcandies(kids) {
  var max = kids[0].candies;
  for (var i = 1; i < kids.length; i++) {
    if (kids[i].candies > max) {
      max = kids[i].candies;
    }
  }
  return max;
}

function getTheRichestKidsName(kids) {
  var max = theMostcandies(kids);
  for (var i = 1; i < kids.length; i++) {
    if (kids[i].candies === max) {
      return kids[i].name;
    }
  }
}
*/
