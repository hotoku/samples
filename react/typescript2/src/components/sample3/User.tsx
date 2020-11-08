import React from "react";

interface Props {}
interface State {}

const sleep = (msec: number) =>
  new Promise((resolve) => setTimeout(resolve, msec));

async function checkPassword(s: string): Promise<boolean> {
  await sleep(1000);
  return s === "abc";
}

class User {
  private _loggedin: boolean;

  constructor() {
    this._loggedin = false;
  }

  public async login(password: string) {
    const ret = await checkPassword(password);
    this._loggedin = ret;
  }

  public get loggedin(): boolean {
    return this._loggedin;
  }

  public logout() {
    this._loggedin = false;
  }
}

export default User;
