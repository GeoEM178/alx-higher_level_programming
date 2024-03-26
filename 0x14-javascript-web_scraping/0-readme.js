#!/usr/bin/node
const fileS = require('fs');
fileS.readFile(process.argv[2], 'utf8', function (errs, data) {
  console.log(errs || data);
});
