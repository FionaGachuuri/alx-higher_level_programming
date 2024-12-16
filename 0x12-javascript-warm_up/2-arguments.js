#!/usr/bin/node
const args = process.argv;
const noOfArgs = args.length - 2;
if (noOfArgs === 0) {
  console.log('No argument');
} else if (noOfArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
