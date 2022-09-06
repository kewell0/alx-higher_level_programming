#!/usr/bin/node

let printTimes = parseInt(process.argv[2]);
if (isNaN(printTimes) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  while (printTimes > 0) {
    console.log('C is fun');
    printTimes--;
  }
}
