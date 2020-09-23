#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const fileName = argv[2];
const text = argv[3];
fs.writeFile(fileName, text, (err, data) => {
  if (err) return console.log(err);
});
