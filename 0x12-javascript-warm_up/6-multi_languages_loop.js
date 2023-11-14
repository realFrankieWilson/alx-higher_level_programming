#!/usr/bin/node
// A script that prints 3 lines by using an array of string and a loop
const words = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
const len = words.length;
let i = 0;
while (i !== len) {
  console.log(words[i]);
  i++;
}
