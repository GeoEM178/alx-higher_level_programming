#!/usr/bin/node
exports.esrever = function (list) {
  let hh = list?.length - 1;
  let u = 0;
  while ((hh - u) > 0) {
    const ahty = list[hh];
    list[hh] = list[u];
    list[u] = ahty;
    u++;
    hh--;
  }
  return list;
};
