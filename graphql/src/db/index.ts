import { existsSync, unlinkSync } from "fs";
import { Database } from "sqlite";
import { Database as Driver } from "sqlite3";

export async function init() {
  if (existsSync(filePath)) unlinkSync(filePath);

  try {
    const db = await getInstance();
    await db.exec(`
      create table teams (
        id integer primary key,
        name text not null
      );

      create table users (
        id integer primary key,
        name text not null,
        email text not null,
        team_id integer not null,
        foreign key (team_id)
        references teams(id)
      );
    `);
    type Team = {
      id: number;
      name: string;
    };
    type User = {
      id: number;
      name: string;
      email: string;
      team_id: number;
    };
    const teams: Team[] = [];
    const users: User[] = [];
    for (let i = 0; i < 3; i++) {
      teams.push({
        id: i,
        name: `team ${i}`,
      });
      users.push({
        id: i,
        name: `user ${i}`,
        email: `user${i}@domain${i}.com`,
        team_id: i,
      });
    }
    for (let i = 0; i < teams.length; i++) {
      await db.run("insert into teams (id, name) values (?, ?)", [
        teams[i].id,
        teams[i].name,
      ]);
    }
    for (let i = 0; i < users.length; i++) {
      await db.run(
        "insert into users (id, name, email, team_id) values (?, ?, ?, ?)",
        [users[i].id, users[i].name, users[i].email, users[i].team_id]
      );
    }
    await db.close();
  } catch (e: any) {
    console.log("error:", JSON.stringify(e));
    throw e;
  }
}

const filePath = "/tmp/temp.sqlite";

export async function getInstance(): Promise<Database> {
  const db = new Database({
    filename: filePath,
    driver: Driver,
  });
  await db.open();
  await db.run("PRAGMA foreign_keys = ON");
  return db;
}
