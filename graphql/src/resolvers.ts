import { getInstance } from "./db";
import DataLoader from "dataloader";

type TeamResolver = {
  id: number;
  name: () => Promise<string>;
  users: () => Promise<UserResolver[]>;
};

type UserResolver = {
  id: number;
  name: string;
  team: () => TeamResolver;
};

export const getUser = async (args: { id: number }): Promise<UserResolver> => {
  const user: any = await userLoader.load(args.id);
  return {
    id: args.id,
    name: user.name,
    team: () => getTeam(user.teamId),
  };
};

export function getTeam(args: { id: number }): TeamResolver {
  return {
    id: args.id,
    name: async () => {
      const db = await getInstance();
      const ret = await db.all("select name from teams where id=?", args.id);
      return ret[0].name;
    },
    users: async () => {
      const db = await getInstance();
      const rows = await db.all("select id from users where teamId=?", args.id);
      const ids = rows.map((row) => row.id);
      return Promise.all(ids.map(getUser));
    },
  };
}

const userLoader = new DataLoader<number, any>(async (ids) => {
  const db = await getInstance();
  const rows = await db.all(
    `select id, name, teamId from users where id in (${ids.join(",")})`
  );
  return ids.map(
    (id) =>
      rows.find((row) => row.id === id) || new Error(`Row not found: ${id}`)
  );
});
