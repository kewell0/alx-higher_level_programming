#!/usr/bin/node

if (process.argv.length === 1) {
  console.log('0');
} else {
  const num = process.argv.slice(2).map(x => parseInt(x));
  num.sort(function (a, b) { return b - a; });
  console.log(num[1]);
}
