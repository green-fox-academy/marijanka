'use strict';

var kids = [
  {name: 'Julika', age: 8, sex: 'female'},
  {name: 'Tiborka', age: 7, sex: 'male'},
  {name: 'Zsolti', age: 6, sex: 'male'},
  {name: 'Gerda', age: 9, sex: 'female'},
  {name: 'Zsomborka', age: 8, sex: 'male'}
];

/*function groupBySex(kids) {
	var output = {};
	kids.forEach(function(kid) {
		if(output[kid.sex] === undefined) {
			output[kid.sex] = [];
		}
		output[kid.sex].push(kid);
	});
	return output;
}*/

function groupBySex (kids) {
  var output = {female: [], male: []};
  kids.forEach(function (kid) {
    output[kid.sex].push(kid);
  });
  return output;
}

groupBySex(kids);


console.log(groupBySex(kids));