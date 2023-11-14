#!/usr/bin/node
/* A script that prints a square
 * Descrpt: The first argument is the size of the square
 *    If the argument can't be converted to an integer, print
 *    "Missing size"
 */
const args = process.argv;
const arg = args.slice(2);
const toNum = parseInt(arg[0]);
const x = 'X';
let i = 0;
if (!(toNum)) {
  console.log('Missing size');
} else {
  for (; i < toNum; i++) {
    console.log(x.repeat(toNum));
  }
}
