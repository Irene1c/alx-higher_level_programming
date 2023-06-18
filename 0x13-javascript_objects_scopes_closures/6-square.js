#!/usr/bin/node
const Sq = require('./5-square.js');

class Square extends Sq {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let r = '';
        for (let j = 0; j < this.width; j++) {
          r += c;
        }
        console.log(r);
      }
    }
  }
}

module.exports = Square;
