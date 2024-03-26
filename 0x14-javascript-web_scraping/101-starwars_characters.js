#!/usr/bin/node
const thereq = require('request');
const swapiURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
thereq(swapiURL, function (rrses, response, dataa) {
  if (!rrses) {
    const chars = JSON.parse(dataa).characters;
    printCharacters(chars, 0);
  }
});

function printCharacters (chars, index) {
  thereq(chars[index], function (rrses, resss, dataa) {
    if (!rrses) {
      console.log(JSON.parse(dataa).name);
      if (index + 1 < chars.length) {
        printCharacters(chars, index + 1);
      }
    }
  });
}
