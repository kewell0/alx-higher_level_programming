#!/usr/bin/node

function factorial (fact) {
  if (fact === 0) {
    return 0;
  } else if (fact === 1) {
    return 1;
  } else {
    return (fact * factorial(fact - 1));
  }
}

const myInt = parseInt(process.argv[2]);

if (isNaN(myInt) || myInt === undefined) {
  console.log('1');
} else {
  console.log(factorial(myInt));
}
