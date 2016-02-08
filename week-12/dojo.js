'use strict';

function parseArguments(command) {
	if (command === '') {
		return {};
	} 
	var splitArgument = command.split('-');
	splitArgument.shift();
	var parsedArguments = {};
	splitArgument.forEach(function (arg) {
		var split = arg.split(' ');
		if (split[1] === '') {split.pop()};
		parsedArguments[split[0]] = parseValue(split[1]);
	}) 
	return parsedArguments;
}

function parseValue(splitArgument) {
	var value = splitArgument;
	if (value === undefined) {
		return true;
	} else if (Number.isNaN(Number(value))) {
		return value;	
	} else {
		return Number(value);
	}	
}

module.exports = parseArguments;

