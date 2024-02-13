#!/usr/bin/node
const OldSquare = require("./5-square");

class Square extends OldSquare {
  charPrint(c) {
    if (!c || c === undefined) {
      c = "X";
    }
    for (let r = 0; r < this.height; r++) {
      let e = "";
      for (let sr = 0; sr < this.width; sr++) {
        e = `${e}${c}`;
      }
      console.log(e);
    }
  }
}

module.exports = Square;
