#!/usr/bin/node
// Imports the reqest module
const request = require('request');
// API endpoint
const url = process.argv.slice(2)[0];
// Initialize counter
let counts = 0;

request.get(url, (error, resp, body) => {
  if (error) {
    console.error(error);
  } else {
    // Converts JSON file to javaScript
    const obj = JSON.parse(body).results;
    for (const movie in obj) {
      const objList = obj[movie].characters;
      for (const i in objList) {
        if (objList[i].includes('18')) {
          counts = counts + 1;
        }
      }
    }
    console.log(counts);
  }
});
