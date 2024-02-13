#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let newT = 0;
  for (let k = 0; k < list.length; k++) {
    if (searchElement === list[k]) {
      newT++;
    }
  }
  return newT;
};
