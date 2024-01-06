#!/usr/bin/node

// Gets the command line arguments
const args = process.argv.slice(2);

// Import the http module
const request = require('request');

// Gets the url from command line arguments
const url = args[0];

// Make a GET request
request.get(url, (error, response) => {
  if (error) {
    throw error;
  } else {
    // Display status code
    console.log('code:', response.statusCode);
  }
});
