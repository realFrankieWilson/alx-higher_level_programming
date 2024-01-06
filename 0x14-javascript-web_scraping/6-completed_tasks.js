#!/usr/bin/node

// Gets the command line arguments
const url = process.argv[2]; // API URL

// Get the request method.
const request = require('request');

// Define tasks
const tasksDict = {};
const tasksList = [];

// Make a GET request to download the file
request(url, function (error, resp, body) {
  if (error) {
    console.error(error);
  }
  const undoneList = JSON.parse(body);
  for (const names in undoneList) {
    const task = undoneList[names];
    if (task.completed === true) {
      tasksList.push(task.userId);
    }
  }
  tasksList.forEach(function (i) { tasksDict[i] = (tasksDict[i] || 0) + 1; });
  console.log(tasksDict);
});
