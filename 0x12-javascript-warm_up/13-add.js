#!/usr/bin/node
/**
 * A function that returns the addition of 2 integers.
 * Description:
 *    The function must be visible from outside.
 *    The name of the function must be add
 */

function add (a, b) {
  return (Number(a) + Number(b));
}

//  Exports the function
module.exports = {
  add
};
