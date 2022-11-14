import createApp from "./server";
import * as portfinder from "portfinder";

async function main(): Promise<void> {
  const app = createApp();
  const port = await portfinder.getPortPromise({
    port: 4000,
  });
  console.log("port =", port);
  app.listen(port);
}

main();
