#!/usr/bin/node

// Gets the command line arguments
const data = process.argv[2];
const path = process.argv[3];

// Get the file system.
const fs = require('fs');
// Get the request method.
const request = require('request');

// Make a GET request to download the file
request(data, 'utf-8').pipe(fs.createWriteStream(path));
