#!/usr/bin/node

const argv1 = parseInt(process.argv[2]);
const argv2 = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}

console.log(add(argv1, argv2));
