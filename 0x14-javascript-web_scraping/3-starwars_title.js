#!/usr/bin/node
const argv = process.argv;
const url = 'https://swapi-api.hbtn.io/api/films/' + argv[2];
const request = require('request');
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
