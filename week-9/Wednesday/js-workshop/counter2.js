'use strict';

function createAdder(start) {
	return function() {
		start++;
		return start;
	}
}

var counter = createAdder(5);
console.log(counter());
console.log(counter());