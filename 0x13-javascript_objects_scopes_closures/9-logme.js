#!/usr/bin/node

let count = -1;
exports.logMe = function (item) {
  let arg = '';
  for (let i = 0; i < item.length; i++) {
    arg += item[i];
  }
  count++;
  console.log(count + ': ' + arg);
};
