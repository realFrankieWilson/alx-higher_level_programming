#!/usr/bin/node

// Gets the command line arguments
const args = process.argv.slice(2);
const path = args[0];

// Gets the file to read from
const getContent = require('fs');

// Reads the content of a file
getContent.readFile(path, 'utf8', (err, contents) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(contents);
});
