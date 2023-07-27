#!/usr/bin/node

// script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filename = process.argv[3];

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(filename, body, 'utf8', (err) => {
      if (err) {
        console.error('Error:', err);
      }
    });
  }
});
