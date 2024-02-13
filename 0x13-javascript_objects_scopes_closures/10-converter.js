#!/usr/bin/node

exports.converter = function (base) {
  return function (neT) {
    return neT.toString(base);
  };
};
