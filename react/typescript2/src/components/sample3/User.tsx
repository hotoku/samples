import React from "react";

interface Props {}
interface State {}

class User {
  private _loggedin: boolean;

  constructor() {
    this._loggedin = false;
  }

  public login(password: string): boolean {
    if (password === "abc") {
      this._loggedin = true;
    } else {
      this._loggedin = false;
    }
    return this._loggedin;
  }
}

export default User;
