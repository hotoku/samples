import React, { useState } from "react";
import "./App.css";
import { Sample1 } from "./components/sample1";
import { Sample2 } from "./components/sample2";
import { Sample3 } from "./components/sample3";
import { Sample4 } from "./components/sample4";
import { Sample5 } from "./components/sample5";
import { Sample6 } from "./components/sample6";
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
          <li>
            <Link to="/4">4</Link>
          </li>
          <li>
            <Link to="/5">5</Link>
          </li>
          <li>
            <Link to="/6">6</Link>
          </li>
        </ul>
        <Line />

        <Switch>
          <Route exact path="/1" render={() => <Sample1 name={"sample1"} />} />
          <Route exact path="/2" render={() => <Sample2 cnt={0} />} />
          <Route path="/3" component={Sample3} />
          <Route exact path="/4" component={Sample4} />
          <Route exact path="/5" component={Sample5} />
          <Route exact path="/6" component={Sample6} />
          <p>no match</p>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
