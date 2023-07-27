#!/usr/bin/node

// script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');

const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];

const url = baseUrl + movieId;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
