import express from "express";
import bodyParser from "body-parser";
import morgan from "morgan";
import * as portfinder from "portfinder";

const app = express();

app.use(bodyParser.json());
app.use(morgan("combined"));

(async () => {
  const port = await portfinder.getPortPromise({
    port: 3000,
  });
  console.log("port =", port);
  app.listen(port);
})();
