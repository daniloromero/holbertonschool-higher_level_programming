#!/usr/bin/node
const myVar = process.argv.slice(2);
const x = Number(myVar[0]);
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
