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

// Check for No argument passed.
if (len <= 1) {
  console.log(0);
} else {
  let biggestNum = args[0];
  let secBig = (args[1]);

  if (secBig > biggestNum) {
    [biggestNum, secBig] = [secBig, biggestNum];
  }

  for (let i = 2; i < len; i++) {
    const currentNum = args[i];

    if (currentNum > biggestNum) {
      secBig = biggestNum;
      biggestNum = currentNum;
    } else if (currentNum > secBig && currentNum !== biggestNum) {
      secBig = currentNum;
    }
  }
  console.log('The second biggest is: ', secBig);
}
