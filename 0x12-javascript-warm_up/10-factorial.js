#!/usr/bin/node
/**
 * A script that computes and prints a factorial.
 * Description:
 *    The first argument is the first integer.
 *    Factorial of NaN is 1.
 */

const args = process.argv.slice(2);
const arg1 = args[0];

//  Check if first argument is an int or not.
function factorial (a) {
  if (isNaN(a)) {
    console.log(1);
    return;
  }

  //  The base condition for the recursion.
  if (a <= 0) {
    return;
  }

  //  Output the value of a, then decrement it by 1.
  console.log(a);
  factorial(a - 1);
}

//  Function call.
factorial(arg1);
