#!/usr/bin/node
// A script that prints a messge dependig
// of the number of arguments passed.

const args = process.argv.length - 2;
if (args == 0) {
	console.log('No argument');
} else if (args == 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
