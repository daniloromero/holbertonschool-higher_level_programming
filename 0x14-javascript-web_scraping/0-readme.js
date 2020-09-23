#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const fileName = argv[2];
fs.readFile(fileName, (err, data) => {
  if (err) {
    throw err;
  }
  console.log(data.toString());
});
