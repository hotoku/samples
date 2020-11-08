import React from "react";
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";
import { Login } from "./sample3/Login";
import { Logout } from "./sample3/Logout";
import User from "./sample3/User";
import Auth from "./sample3/Auth";

interface State {
  user: User;
}

/* シンプルなlogin/logoutの画面遷移 */

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
            <Route
              exact
              path="/3/logout"
              render={() => <Logout user={this.user} />}
            />
            <Auth user={this.user}>
              <p>logged in</p>
              <Link to="/3/logout">logout</Link>
            </Auth>
          </Switch>
        </BrowserRouter>
      </div>
    );
  };
}
