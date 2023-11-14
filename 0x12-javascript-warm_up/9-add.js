#!/usr/bin/node
/**
 * A script that prints the additin of 2 integers.
 * Description:
 *    The first argument is the first integer.
 *    The second argument is the second integer.
 */
const args = process.argv.slice(2);
let a = args[0];
let b = args[1];
function add(a, b) {
  console.log(a + b);
}

add(a, b);
