#!/usr/bin/node
if (!process.argv[2] || isNaN(process.argv[2])) {
  const logString = "Missing size";
  console.log(logString);
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log("X".repeat(x));
    i++;
  }
}
