#!/usr/bin/node
const the_req = require('request');
the_req.get(process.argv[2]).on('response', function (responsees) {
  console.log(`code: ${the_req.statusCode}`);
});
