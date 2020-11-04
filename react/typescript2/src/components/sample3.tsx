import React from "react";
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import { Login } from "./sample3/Login";
import User from "./sample3/User";

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
              path="/login"
              render={() => <Login user={this.user} />}
            />
            <Link to="/login">login</Link>
          </Switch>
        </BrowserRouter>
      </div>
    );
  };
}
