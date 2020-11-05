const sleep = (msec: number) =>
  new Promise((resolve) => setTimeout(resolve, msec));

async function f() {
  console.log("start");
  await sleep(2000);
  console.log("end");
}

f();
