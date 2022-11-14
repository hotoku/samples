import { getInstance } from "./db";

async function main() {
  const db = await getInstance();
  const ret = await db.all("select * from users where id=?", 1);
  console.log(ret);
}

main();
