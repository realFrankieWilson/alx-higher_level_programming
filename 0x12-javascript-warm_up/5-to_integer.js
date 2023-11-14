#!/usr/bin/node
/* A script that converts string to an integer
 * and prints them out.
 */
const args = process.argv;
const arg = args.slice(2);
const toNum = parseInt(arg[0]);
if (isNaN(toNum)) {
  console.log('Not a number');
} else {
  console.log(toNum);
}
