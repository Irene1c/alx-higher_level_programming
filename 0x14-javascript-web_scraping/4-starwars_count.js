#!/usr/bin/node

//  script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');

const url = process.argv[2];
const charId = 18;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const allMovies = data.results;
    let count = 0;
    for (const movie in allMovies) {
      const allChars = allMovies[movie].characters;
      for (const character in allChars) {
        if (allChars[character].includes(charId)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
