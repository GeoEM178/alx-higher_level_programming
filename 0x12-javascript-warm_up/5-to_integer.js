#!/usr/bin/node
if (isNaN(process.argv[2]) || !process.argv[2]) {
  const logString = "Not a number";
  console.log(logString);
} else {
  console.log("My number:", parseInt(process.argv[2]));
}
