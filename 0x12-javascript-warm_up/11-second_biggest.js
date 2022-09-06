#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const myInts = [];
  for (let i = 2; i < size; i++) {
    myInts[i - 2] = parseInt(process.argv[i]);
  }
  myInts.sort(function (a, b) { return b - a; });
  console.log(myInts[1]);
}
