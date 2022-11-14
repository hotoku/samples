import { unlinkSync, existsSync } from "fs";
import { Database } from "sqlite";
import { Database as Driver } from "sqlite3";

function dbPath(): string {
  return "./db.sqlite";
}

export async function getInstance(): Promise<Database> {
  const db = new Database({
    filename: dbPath(),
    driver: Driver,
  });
  await db.open();
  await db.run("PRAGMA foreign_keys = ON");
  return db;
}

export function remove() {
  const path = dbPath();
  if (existsSync(path)) {
    unlinkSync(dbPath());
  }
}

export async function query(sql: string, ...args: any[]): Promise<any[]> {
  console.log("query:", sql);
  const db = await getInstance();
  return await db.all(sql, ...args);
}
