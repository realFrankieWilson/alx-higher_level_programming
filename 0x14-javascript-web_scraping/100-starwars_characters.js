#!/usr/bin/node

// Gets the command line arguments
const movieId = process.argv[2]; // character id

// Get the request method.
const request = require('request');
const api = 'https://swapi-api.alx-tools.com/api/filmes/';

request.get(api + movieId, (error, resp, body) => {
  if (error) console.error(error);

  const data = JSON.parse(body);
  const chars = data.characters;

  chars.forEach(charId => {
    request.get(charId, (error, resp, body) => {
      if (error) console.error(error);

      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  });
});
