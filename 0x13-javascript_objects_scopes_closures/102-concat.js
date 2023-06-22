#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, file1) => {
  if (err) {
    console.error('Error reading file1');
  }

  fs.readFile(process.argv[3], 'utf8', (err, file2) => {
    if (err) {
      console.error('Error reading file2');
    }

    const concatFile = file1 + file2;

    fs.writeFile(process.argv[4], concatFile, (err) => {
      if (err) {
        console.error('Error writing file');
      }
    });
  });
});
