import express from "express";
import { buildSchema, GraphQLSchema } from "graphql";
import { graphqlHTTP } from "express-graphql";
import bodyParser from "body-parser";
import morgan from "morgan";
import { queryType } from "./resolvers";
import { userLoader, teamLoader, teamUsersLoader } from "./data-loaders";

function createApp(): express.Express {
  const app = express();

  app.use(bodyParser.json());
  app.use(morgan("combined"));
  app.use("/graphql", (req, res) => {
    const loaders = {
      userLoader: userLoader(),
      teamLoader: teamLoader(),
      teamUsersLoader: teamUsersLoader(),
    };

    return graphqlHTTP({
      schema: new GraphQLSchema({ query: queryType }),
      graphiql: true,
      context: { loaders },
    })(req, res);
  });

  return app;
}

export default createApp;
