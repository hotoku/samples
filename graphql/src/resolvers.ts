import { getInstance } from "./db";
import { BatchLoadFn, CacheMap } from "dataloader";

type TeamResolver = {
  id: number;
  name: () => Promise<string>;
  users: () => Promise<UserResolver[]>;
};

type UserResolver = {
  id: number;
  name: () => Promise<string>;
  team: () => Promise<TeamResolver>;
};

export function getUser(args: { id: number }): UserResolver {
  return {
    id: args.id,
    name: async () => {
      const db = await getInstance();
      const ret = await db.all("select name from users where id=?", args.id);
      return ret[0].name;
    },
    team: async () => {
      const db = await getInstance();
      const ret = await db.all("select teamId from users where id=?", args.id);
      const teamId = ret[0].teamId;
      return getTeam({ id: teamId });
    },
  };
}

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
      const ret = await db.all("select id from users where teamId=?", args.id);
      return ret.map((x) => getUser({ id: x.id }));
    },
  };
}
