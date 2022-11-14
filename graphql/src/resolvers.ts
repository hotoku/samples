import { getInstance } from "./db";
import DataLoader from "dataloader";

type TeamResolver = {
  id: number;
  name: string;
  users: () => Promise<UserResolver[]>;
};

type UserResolver = {
  id: number;
  name: string;
  team: () => Promise<TeamResolver>;
};

export async function getUser(args: { id: number }): Promise<UserResolver> {
  const user = await userLoader.load(args.id);
  return {
    id: args.id,
    name: user.name,
    team: async () => getTeam({ id: user.teamId }),
  };
}

export async function getTeam(args: { id: number }): Promise<TeamResolver> {
  const team = await teamLoader.load(args.id);
  return {
    id: args.id,
    name: team.name,
    users: async () => Promise.all(team.userIds.map((id) => getUser({ id }))),
  };
}

const userLoader = new DataLoader<
  number,
  { id: number; name: string; teamId: number }
>(async (ids) => {
  const db = await getInstance();
  const rows = (await db.all(
    `select id, name, teamId from users where id in (${ids.join(",")})`
  )) as { id: number; name: string; teamId: number }[];
  return ids.map(
    (id) =>
      rows.find((row) => row.id === id) || new Error(`Row not found: ${id}`)
  );
});

const teamLoader = new DataLoader<
  number,
  { id: number; name: string; userIds: number[] }
>(async (ids) => {
  const db = await getInstance();
  const rows = (await db.all(
    `select id, name from teams where id in (${ids.join(",")})`
  )) as { id: number; name: string }[];
  const map = new Map<
    number,
    { id: number; name: string; userIds: number[] }
  >();
  for (const row of rows) {
    map.set(row.id, { userIds: [], ...row });
  }
  const rows2 = (await db.all(
    `select id as userId, teamId from users where teamId in (${ids.join(",")})`
  )) as { userId: number; teamId: number }[];
  for (const row of rows2) {
    const team = map.get(row.teamId);
    if (!team) continue;
    team.userIds.push(row.userId);
  }
  return ids.map((id) => map.get(id) || new Error(`not found team id: ${id}`));
});
