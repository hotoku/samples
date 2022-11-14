import { getInstance, remove } from "./db";

async function createTables(): Promise<void> {
  const db = await getInstance();
  const sql = `
    create table teams (
      id integer primary key,
      name text not null
    );
    create table users (
      id integer primary key,
      name text not null,
      team_id integer not null,
      foreign key (team_id) references teams(id)
    );
  `;
  await db.exec(sql);
}

async function loadTeams(): Promise<number> {
  const db = await getInstance();
  const teams = ["abc", "def", "ghi"];
  const sql = `
    insert into teams (name) values (?)
  `;
  for (const team of teams) {
    await db.run(sql, team);
  }
  return teams.length;
}

async function loadUsers(n: number): Promise<void> {
  const db = await getInstance();
  const names = [] as string[];
  for (let i = 0; i < 100; i++) {
    names.push("user-" + i);
  }
  const sql = `
    insert into users (name, team_id) values (?, ?)
  `;
  let team = 0;
  for (const name of names) {
    await db.run(sql, name, team + 1);
    team += 1;
    if (team === n) {
      team = 0;
    }
  }
}

async function main() {
  remove();
  await createTables();
  const n = await loadTeams();
  await loadUsers(n);
}

main();
