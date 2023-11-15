#!/usr/bin/node
/**
 * A script that prints the additin of 2 integers.
 * Description:
 *    The first argument is the first integer.
 *    The second argument is the second integer.
 */

const args = process.argv.slice(2);
const arg1 = args[0];
const arg2 = args[1];

function add (a, b) {
  console.log(Number(a) + Number(b));
}

add(arg1, arg2);
