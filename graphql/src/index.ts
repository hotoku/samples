import express from "express";
import bodyParser from "body-parser";
import morgan from "morgan";
import * as portfinder from "portfinder";
import { UsersResolver } from "./users/users.resolvers";
import { TeamsResolver } from "./teams/teams.resolvers";
import { buildSchema } from "type-graphql";
import { graphqlHTTP } from "express-graphql";
import { init } from "./db";

async function run() {
  await init();

  const port = await portfinder.getPortPromise({
    port: 3000,
  });
  console.log("port =", port);

  const app = express();

  app.use(bodyParser.json());
  app.use(morgan("combined"));

  const schema = await buildSchema({
    resolvers: [UsersResolver, TeamsResolver],
    emitSchemaFile: true,
  });
  app.use(
    "/graphql",
    graphqlHTTP({
      schema: schema,
      graphiql: true,
    })
  );
  app.listen(port);
}

run();
