'use strict';

function printEverything(a, b, c) {
	console.log(a, b, c, this);
}

printEverything(1, 2, 3);

var obj = {
	kacsa : 1,
	printEverything: printEverything
}

obj.printEverything(1, 2, 3);

