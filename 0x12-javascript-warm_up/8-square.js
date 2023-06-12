#!/usr/bin/node

if (Number(process.argv[2])) {
  for (let i = 0; i < process.argv[2]; i++) {
    let r = '';
    for (let j = 0; j < process.argv[2]; j++) {
      r += 'X';
    }
    console.log(r);
  }
} else {
  console.log('Missing size');
}
