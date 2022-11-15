import express from "express";
import { buildSchema } from "graphql";
import { graphqlHTTP } from "express-graphql";
import bodyParser from "body-parser";
import morgan from "morgan";
import { getTeam, getUser } from "./resolvers";
import { userLoader, teamLoader } from "./data-loaders";

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

  // todo: 現在の実装だと、キャッシュがリクエストをまたいで保存されてしまうので解決策を調べる
  const rootValue = {
    getUser: getUser,
    getTeam: getTeam,
  };

  app.use(bodyParser.json());
  app.use(morgan("combined"));
  app.use("/graphql", (req, res) => {
    const loaders = {
      userLoader,
      teamLoader,
    };

    return graphqlHTTP({
      schema: schema,
      rootValue: rootValue,
      graphiql: true,
      context: loaders,
    })(req, res);
  });

  return app;
}

export default createApp;
