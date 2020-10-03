#!/usr/bin/node
const myVar = process.argv.slice(2);
if (myVar.length <= 1) {
  console.log(0);
} else {
  const myArr = myVar.map(x => parseInt(x));
  myArr.sort((a, b) => a - b);
  myArr.pop();
  console.log(Math.max(...myArr));
}
