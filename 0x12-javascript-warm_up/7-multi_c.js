#!/usr/bin/node
let x = process.argv[2];
x = parseInt(x);
if (isNaN(x)) {
    console.log('Missing number of occurrences');
} else {
  for (let a = 0; a > x; a++) {
    console.log('C is fun');
  }
}