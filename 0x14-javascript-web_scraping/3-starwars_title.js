#!/usr/bin/node
const thereq = require('request');
const epnumss = process.argv[2];
const swapi_url = 'https://swapi-api.hbtn.io/api/films/';
thereq(swapi_url + epnumss, function (ersors, the_res, body) {
  if (ersors) {
    console.log(ersors);
  } else if (the_res.statusCode === 200) {
    const jsonthe_responses = JSON.parse(body);
    console.log(jsonthe_responses.title);
  } else {
    console.log('Error code: ' + the_res.statusCode);
  }
});
