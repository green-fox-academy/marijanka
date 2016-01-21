'use strict';

var array = ['apple', 'pear', 'melon', 'carrot', 'grape']

function deletel(array) {
	var newArray = [];
	array.forEach(function(elem) {
		if (elem !== 'carrot') {
			newArray.push(elem);
		};
	array = newArray;
	return array;
	});
}

function deletel2(array) {
	array.splice(array.indexOf('carrot'), 1);
	return array;
}

//console.log(deletel2(array));
console.log(deletel(array));