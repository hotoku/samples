import React from "react";
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import { Login } from "./sample3/Login";
import User from "./sample3/User";
import Auth from "./sample3/Auth";

interface State {
  user: User;
}

export class Sample3 extends React.Component<{}, State> {
  private user: User;

  constructor(props: {}) {
    super(props);
    this.user = new User();
  }

  render = () => {
    return (
      <div>
        <p>sample3</p>
        <BrowserRouter>
          <Switch>
            <Route
              exact
              path="/3/login"
              render={() => <Login user={this.user} />}
            />
            <Auth user={this.user}>
              <p>logged in</p>
            </Auth>
          </Switch>
        </BrowserRouter>
      </div>
    );
  };
}
