#!/usr/bin/node
/**
 * A script that computes and prints a factorial.
 * Description:
 *    The first argument is the first integer.
 *    Factorial of NaN is 1.
 */

const args = process.argv.slice(2);

function factorial (a) {
  return a === 0 || isNaN(a) ? 1 : a * factorial(a - 1);
}

console.log(factorial(args));
