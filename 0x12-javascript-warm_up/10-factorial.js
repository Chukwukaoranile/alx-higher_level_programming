#!/usr/bin/node
let number = parseInt(process.argv[2]);
function fact (number) {
	  if (number > 0) return (number * fact(number - 1));
	    return (1);
}
if (isNaN(number)) number = 1;
console.log(fact(number));
