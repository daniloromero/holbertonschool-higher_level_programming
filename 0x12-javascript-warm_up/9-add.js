#!/usr/bin/node
const myVar = process.argv.slice(2);
const x = Number(myVar[0]);
const y = Number(myVar[1]);
console.log(x + y);
