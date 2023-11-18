#!/usr/bin/node
/**
 * A script that searches the second beiggest integer in the list of argument
 * Description:
 *   If no argument passed, print 0.
 *   If the number of arguments is 1, print 0.
 */

//   Get input from the command line argument.
const args = process.argv.slice(2);
const len = args.length;

const elem = [];

if (!(args[0])) {
  console.log(0);
} else {
  for (let i = 2; i < len; i++) {
    elem.push(args[i]);
  }
  elem.sort(function (a, b) {
    return a - b;
  });
  elem.pop();
  const check = elem.slice(-1);
  const toNum = parseInt(check);
  console.log(Number(toNum));
}
