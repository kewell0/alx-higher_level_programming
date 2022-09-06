#!/usr/bin/node

let size = parseInt(process.argv[2]);
if (isNaN(size) || process.argv[2] === undefined) {
  console.log('Missing size');
}
let myString = 'X';
for (let i = 0; i < size - 1; i++) {
  myString += 'X';
}
while (size > 0) {
  console.log(myString);
  size--;
}
