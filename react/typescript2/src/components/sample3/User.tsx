import React from "react";

interface Props {}
interface State {}

const sleep = (msec: number) =>
  new Promise((resolve) => setTimeout(resolve, msec));

async function checkPassword(s: string): Promise<boolean> {
  // await sleep(1000);
  return new Promise(() => s === "abc");
}

class User {
  private _loggedin: boolean;

  constructor() {
    this._loggedin = false;
  }

  public async login(password: string) {
    console.log("login start");
    const ret = await checkPassword(password);
    this._loggedin = ret;
    console.log("login end");
  }
}

export default User;
