#!/usr/bin/node
const Rectang = require('./5-rectangle');
class Square extends Rectang {

  charPrint(c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.size; i++) {
      console.log(c.repeat(this.size));
    }
    }
  }
}
module.exports = Square;