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
    for (let w = 0; w < this.height; w++) {
      let s = "";
      for (let e = 0; e < this.width; e++) {
        v += "X";
      }
      console.log(v);
    }
  }

  rotate() {
    const justTemp = this.width;
    this.width = this.height;
    this.height = justTemp;
  }

  double() {
    const dupelWidth = this.width * 2;
    this.width = dupelWidth;
    const dupelHeight = this.height * 2;
    this.height = dupelHeight;
  }
}

module.exports = Rectangle;
