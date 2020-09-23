#!/usr/bin/node
const myVar = process.argv.slice(2);
const x = parseInt(myVar[0]);
function factorial (y) {
  if (isNaN(y)) {
    return 1;
  }
  if (y === 0) {
    return 1;
  } else {
    return (y * factorial(y - 1));
  }
}
console.log(factorial(x));
