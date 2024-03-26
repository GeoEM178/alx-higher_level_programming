#!/usr/bin/node

const thereq = require('request');
const swapi_url = 'https://swapi-api.hbtn.io/api/films/';
const id = process.argv[2];
thereq.get(swapi_url + id, function (err, res, data) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(data);
  const dd = data.characters;
  for (const i of dd) {
    thereq.get(i, function (err, res, data1) {
      if (err) {
        console.log(err);
      }
      const data1 = JSON.parse(data1);
      console.log(data1.name);
    });
  }
});
