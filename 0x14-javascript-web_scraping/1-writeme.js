#!/usr/bin/node

// Gets the command line arguments
const args = process.argv.slice(2);
const path = args[0];
const data = args[1];

// Writes data to a file
const fs = require('fs');

// wwirte the data to the file
fs.writeFile(path, data, 'utf8', (err) => {
  if (err) throw err;
});
