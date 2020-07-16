import React from "react";
import "./App.css";

import { BrowserRouter, Link, Route, Switch } from "react-router-dom";

function HelloA() {
  return <h1>HelloA</h1>;
}

function HelloB() {
  return <h1>HelloB</h1>;
}

function Home() {
  return <h1>Home</h1>;
}

class Hello extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <ul>
            <li>
              <Link to="/hello-a">HelloA</Link>
            </li>
            <li>
              <Link to="/hello-b">HelloB</Link>
            </li>
          </ul>
          <Switch>
            <Route path="/hello-a" component={HelloA} />
            <Route path="/hello-b" component={HelloB} />
            <Route path="*" component={Home} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default Hello;
