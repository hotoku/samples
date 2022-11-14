import express from "express";
import { buildSchema } from "graphql";
import { graphqlHTTP } from "express-graphql";
import bodyParser from "body-parser";
import morgan from "morgan";
import { getInstance } from "./db";

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

function getUser(args: { id: number }): UserResolver {
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

function getTeam(args: { id: number }): TeamResolver {
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
      console.log(ret);
      return ret.map((x) => getUser({ id: x.id }));
    },
  };
}

function createApp(): express.Express {
  const app = express();

  const schema = buildSchema(`
    type User {
      id: Int
      name: String
      team: Team
    }
    type Team {
      id: Int
      name: String
      users: [User]
    }
    type Query {
      getUser(id: Int!): User
      getTeam(id: Int!): Team
    }
  `);

  const rootValue = {
    getUser: getUser,
    getTeam: getTeam,
  };

  app.use(bodyParser.json());
  app.use(morgan("combined"));
  app.use(
    "/graphql",
    graphqlHTTP({
      schema: schema,
      rootValue: rootValue,
      graphiql: true,
    })
  );

  return app;
}

export default createApp;
