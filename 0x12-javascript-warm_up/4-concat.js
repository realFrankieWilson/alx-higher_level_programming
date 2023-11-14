#!/usr/bin/node
/* a string that concatenate to argments to it
 * and prints them out.
 */
const args = process.argv;
const arg = args.slice(2);
console.log(`${arg[0]} is ${arg[1]}`);
