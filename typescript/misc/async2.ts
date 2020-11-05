async function checkPassword(s: string): Promise<boolean> {
  return s === "abc";
}

async function f() {
  const ret = await checkPassword("xyz");
  console.log(ret);
}

f();
