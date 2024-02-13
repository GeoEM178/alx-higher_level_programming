#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w < 0 || h < 0) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let q = 0; q < this.height; q++) {
      let b = "";
      for (let l = 0; l < this.width; l++) {
        b = `${b}X`;
      }
      console.log(b);
    }
  }
}

module.exports = Rectangle;
