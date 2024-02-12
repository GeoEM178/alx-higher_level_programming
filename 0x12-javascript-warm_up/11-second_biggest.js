#!/usr/bin/node
if (process.argv.length <= 3) {
  let stringOf0 = "0";
  console.log(stringOf0);
} else {
  const arr = process.argv.slice(2).map(Number);
  const second = arr.sort(function (a, b) {
    const abs = b - a;
    return abs;
  })[1];
  console.log(second);
}
