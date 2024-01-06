#!/usr/bin/node
// Impots the request module
const request = require('request');

// Gets episode number from line arguments
const episodeNum = process.argv.slice(2)[0];

// API endpoint
const app = 'https://swapi-api.hbtn.io/api/films/';

request.get(app + episodeNum, (error, resp, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
