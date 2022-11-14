import express from "express";
import { buildSchema } from "graphql";
import { graphqlHTTP } from "express-graphql";
import bodyParser from "body-parser";
import morgan from "morgan";

function createApp(): express.Express {
  const app = express();

  const schema = buildSchema(`
    type Query {
      hello(name: String): String
    }
  `);

  const rootValue = {
    hello: (args: { name: string }) => {
      return `Hello ${args.name}`;
    },
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
