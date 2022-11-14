import express from "express";
import { buildSchema } from "graphql";
import { graphqlHTTP } from "express-graphql";
import bodyParser from "body-parser";
import morgan from "morgan";
import { getInstance } from "./db";

function getUser(args: { id: number }): {
  id: number;
  name: () => Promise<string>;
} {
  return {
    id: args.id,
    name: async () => {
      const db = await getInstance();
      const ret = await db.all("select * from users where id=?", args.id);
      return ret[0].name;
    },
  };
}

function createApp(): express.Express {
  const app = express();

  const schema = buildSchema(`
    type User {
      id: Int
      name: String
    }
    type Query {
      getUser(id: Int!): User
    }
  `);

  const rootValue = {
    getUser: getUser,
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
