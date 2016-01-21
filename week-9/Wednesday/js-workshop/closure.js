'use strict';


function createCounter() {
	var count = 0;
	return function() {
		count++;
		return count;
	}
}

var valami = createCounter();
console.log(valami);
console.log(valami());
console.log(valami());

var valami2 = createCounter();
console.log(valami2());
console.log(valami2());