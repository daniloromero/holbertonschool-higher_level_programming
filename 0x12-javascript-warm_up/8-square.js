#!/usr/bin/node
const myVar =  process.argv.slice(2);
const x = Number(myVar[0]);
const str = 'X'
if (isNaN(x)) {
	console.log('Missing size');
} else {
	for (let i = 0; i < x; i++) {
		console.log(str.repeat(x));
	}
}
