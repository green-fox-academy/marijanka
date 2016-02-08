'use strict';

var parseArguments = require('./dojo');
var test = require('tape');

test('is exists', function(t) {
	t.deepEqual(parseArguments(''), {});
	t.end();
});

test('-L works', function(t) {
	t.deepEqual(parseArguments('prog -L'), {L: true});
	t.end();
});

test('-A works', function(t) {
	t.deepEqual(parseArguments('prog -A'), {A: true});
	t.end();
});

test('-A 100', function(t) {
	t.deepEqual(parseArguments('prog -A 100'), {A: 100});
	t.end();
});

test('-W cica', function(t) {
	t.deepEqual(parseArguments('prog -W cica'), {W: "cica"});
	t.end();
});

test('-L -A', function(t) {
	t.deepEqual(parseArguments('prog -L -A'), {L:true, A:true});
	t.end();
});

test('-L -A 100 -W cica', function(t) { 
	t.deepEqual(parseArguments('prog -L -A 100 -W cica'), {L:true, A: 100, W: 'cica'});
	t.end();
});
