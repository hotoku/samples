import React from "react";
import "./App.css";
import { Sample1 } from "./components/sample1";
import { Sample2 } from "./components/sample2";
import { Sample3 } from "./components/sample3";
import { BrowserRouter, Route, Link, Switch } from "react-router-dom";

const Line = () => {
  return (
    <hr
      style={{
        color: "black",
        backgroundColor: "black",
        height: 1,
      }}
    />
  );
};

function App() {
  return (
    <div>
      <BrowserRouter>
        <ul>
          <li>
            <Link to="/1">1</Link>
          </li>
          <li>
            <Link to="/2">2</Link>
          </li>
          <li>
            <Link to="/3">3</Link>
          </li>
        </ul>
        <Line />

        <Switch>
          <Route exact path="/1" render={() => <Sample1 name={"sample1"} />} />
          <Route exact path="/2" render={() => <Sample2 cnt={0} />} />
          <Route exact path="/3" component={Sample3} />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
