import express from "express";
import bodyParser from "body-parser";
import morgan from "morgan";
import * as portfinder from "portfinder";
import { graphqlHTTP } from "express-graphql";
import { buildSchema } from "graphql";

const app = express();

app.use(bodyParser.json());
app.use(morgan("combined"));

const schema = buildSchema(`
  type Query {
    rollDice(num: Int!, numSides: Int): [Int]
  }
`);

const root = {
  rollDice: ({
    num,
    numSides,
  }: {
    num: number;
    numSides: number | undefined;
  }) => {
    const ret = [] as number[];
    console.log("num =", num);
    for (let i = 0; i < num; i++) {
      const v = 1 + Math.floor(Math.random() * (numSides || 6));
      console.log(v);
      ret.push(v);
    }
    return ret;
  },
};

(async () => {
  const port = await portfinder.getPortPromise({
    port: 3000,
  });
  console.log("port =", port);
  app.use(
    "/graphql",
    graphqlHTTP({
      schema: schema,
      rootValue: root,
      graphiql: true,
    })
  );
  app.listen(port);
})();
