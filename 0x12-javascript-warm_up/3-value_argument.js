#!/usr/bin/node
// A script that prints the first argument
// passed to it.
const args = process.argv;
if (!(args[2])) {
  console.log('No argument');
} else if (args[2]) {
  console.log(args[2]);
}
