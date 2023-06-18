#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      Object.create(Rectangle);
    } else if (w === undefined || h === undefined) {
      Object.create(Rectangle);
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let r = '';
      for (let j = 0; j < this.width; j++) {
        r += 'X';
      }
      console.log(r);
    }
  }

  rotate () {
    this.temp = this.height;
    this.height = this.width;
    this.width = this.temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
