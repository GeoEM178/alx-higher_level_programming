#!/usr/bin/node
let rkm = 0;

exports.logMe = function (item) {
  console.log(`${rkm + ':'} ${item}`);
  rkm++;
};
