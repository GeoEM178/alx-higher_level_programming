#!/usr/bin/node
const dict = require('./101-data').dict;

const allarr = Object.entries(dict);
const kyem = Object.values(dict);
const kyemUniq = [...new Set(kyem)];
const newDict = {};
for (const j in kyemUniq) {
  const arr = [];
  for (const k in allarr) {
    if (allarr[k][1] === kyemUniq[j]) {
      arr.unshift(allarr[k][0]);
    }
  }
  newDict[kyemUniq[j]] = arr;
}
console.log(newDict);
