import DataLoader from "dataloader";
import { query } from "./db";

export function userLoader(): DataLoader<
  number,
  { id: number; name: string; teamId: number }
> {
  return new DataLoader<number, { id: number; name: string; teamId: number }>(
    async (ids) => {
      const rows = (await query(
        `select id, name, teamId from users where id in (${ids.join(",")})`
      )) as { id: number; name: string; teamId: number }[];
      return ids.map(
        (id) =>
          rows.find((row) => row.id === id) || new Error(`Row not found: ${id}`)
      );
    }
  );
}

export function teamLoader(): DataLoader<
  number,
  { id: number; name: string; userIds: number[] }
> {
  return new DataLoader<
    number,
    { id: number; name: string; userIds: number[] }
  >(async (ids) => {
    const rows = (await query(
      `select id, name from teams where id in (${ids.join(",")})`
    )) as { id: number; name: string }[];
    const map = new Map<
      number,
      { id: number; name: string; userIds: number[] }
    >();
    for (const row of rows) {
      map.set(row.id, { userIds: [], ...row });
    }
    const rows2 = (await query(
      `select id as userId, teamId from users where teamId in (${ids.join(
        ","
      )})`
    )) as { userId: number; teamId: number }[];
    for (const row of rows2) {
      const team = map.get(row.teamId);
      if (!team) continue;
      team.userIds.push(row.userId);
    }
    return ids.map(
      (id) => map.get(id) || new Error(`not found team id: ${id}`)
    );
  });
}

export function teamUsersLoader(): DataLoader<number, number[]> {
  return new DataLoader<number, number[]>(async (ids) => {
    return [[1]];
  });
}
