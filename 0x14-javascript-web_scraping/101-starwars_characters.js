#!/usr/bin/node

// Gets the command line arguments
const movieId = process.argv[2]; // character id

// Get the request method.
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/filmes/';

request.get(api + movieId, (error, resp, body) => {
  if (!error) {
    const chars = JSON.parse(body).characters;
    chars.forEach((charData, i) => {
      request(charData, (error, resp, body) => {
        if (!error) console.log(JSON.parse(body).name);
        if (i === chars.length - 1);
      });
    });
  }
});
