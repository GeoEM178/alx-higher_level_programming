#!/usr/bin/node
const the_req = require('request');
const dikle_s = require('fs');
the_req(process.argv[2]).pipe(dikle_s.createWriteStream(process.argv[3]));
