#!/usr/bin/node
/* A script that prints X times "C is fun"
 * and prints them out.
 * Descrpt: X is the first argument of the script.
 *    If the argument can't be converted to an integer, print
 *    "Missing number of occurrences"
 */
const args = process.argv;
const arg = args.slice(2);
let toNum = parseInt(arg[0]);
if (!(toNum)) {
  console.log('Missing number of occurrences');
} else {
  for (;toNum > 0; toNum--) {
    console.log('C is fun');
  }
}
