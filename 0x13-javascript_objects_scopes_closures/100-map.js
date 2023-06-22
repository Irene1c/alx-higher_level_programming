#!/usr/bin/node

const { list } = require('./100-data.js');
console.log(list);
const MulIndex = list.map((element, index) => (element * index));
console.log(MulIndex);
