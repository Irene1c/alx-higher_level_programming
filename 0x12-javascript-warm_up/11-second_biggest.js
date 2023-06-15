#!/usr/bin/node

if (process.argv.length === 2) {
  console.log(0);
} else if (process.argv.length === 3) {
  console.log(0);
} else {
  const arr = [];
  let num;
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(process.argv[i]);
    num = arr.sort((a, b) => b - a);
  }
  console.log(num[1]);
}
