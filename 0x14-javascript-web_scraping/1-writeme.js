#!/usr/bin/node
const fileS = require('fs');
fileS.writeFile(process.argv[2], process.argv[3], errs => {
  if (errs) console.log(errs);
});
