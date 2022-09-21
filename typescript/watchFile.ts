import fs from "fs";

fs.watchFile(
  "sample.txt",
  { persistent: true, interval: 10 },
  (curr: any, prev: any) => {
    console.log(`changed
curr=${JSON.stringify(curr)}
prev=${JSON.stringify(prev)}`);
  }
);
