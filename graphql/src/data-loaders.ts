import DataLoader from "dataloader";
import { query } from "./db";

export type UserRecord = {
  id: number;
  name: string;
  teamId: number;
};

export type TeamRecord = {
  id: number;
  name: string;
};

export function userLoader(): DataLoader<number, UserRecord> {
  return new DataLoader<number, UserRecord>(async (ids) => {
    const rows = (await query(
      `select id, name, teamId from users where id in (${ids.join(",")})`
    )) as UserRecord[];
    return ids.map(
      (id) =>
        rows.find((row) => row.id === id) ||
        new Error(`User not found for: ${id}`)
    );
  });
}

export function teamLoader(): DataLoader<number, TeamRecord> {
  return new DataLoader<number, TeamRecord>(async (ids) => {
    const rows = (await query(
      `select id, name from teams where id in (${ids.join(",")})`
    )) as { id: number; name: string }[];
    const map = new Map<number, TeamRecord>();
    for (const row of rows) {
      map.set(row.id, { ...row });
    }
    return ids.map(
      (id) => map.get(id) || new Error(`Team not found for: ${id}`)
    );
  });
}

export function teamUsersLoader(): DataLoader<number, number[]> {
  return new DataLoader<number, number[]>(async (teamIds) => {
    const sql = `select id as userId, teamId from users
      where teamId in (${teamIds.join(",")})`;
    const rows = (await query(sql)) as { userId: number; teamId: number }[];
    const map = new Map<number, number[]>();
    for (const row of rows) {
      const array = map.get(row.teamId);
      if (array === undefined) {
        map.set(row.teamId, [row.userId]);
      } else {
        array.push(row.userId);
      }
    }
    const ret = teamIds.map(
      (id) => map.get(id) || new Error(`not found team id: ${id}`)
    );
    return ret;
  });
}

export type MyDataLoader = {
  userLoader: DataLoader<number, UserRecord>;
  teamLoader: DataLoader<number, TeamRecord>;
  teamUsersLoader: DataLoader<number, number[]>;
};
