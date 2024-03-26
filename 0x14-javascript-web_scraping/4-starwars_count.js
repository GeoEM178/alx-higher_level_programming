#!/usr/bin/node
const the_req = require('request');
the_req(process.argv[2], function (n_error, res, data) {
  if (!n_error) {
    const ress = JSON.parse(data).results;
    console.log(ress.reduce((num, n_data) => {
      return n_data.characters.find((char) => char.endsWith('/18/'))
        ? num + 1
        : num;
    }, 0));
  }
});
