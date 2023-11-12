#!/usr/bin/node

// script that prints all characters of a Star Wars movie

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    for (const charUrl of data.characters) {
      request.get(charUrl, (error, response, body2) => {
        if (error) {
          console.error(error);
        } else {
          const characters = JSON.parse(body2);
          console.log(characters.name);
        }
      });
    }
  }
});
