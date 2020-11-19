import React, { useState } from "react";
import "./App.css";
import { Sample1 } from "./components/sample1";
import { Sample2 } from "./components/sample2";
import { Sample3 } from "./components/sample3";
import { Sample4 } from "./components/sample4";
import { Sample5 } from "./components/sample5";
import { Sample6 } from "./components/sample6";
import { Sample7 } from "./components/sample7";
import { Sample8 } from "./components/sample8";
import { Sample9 } from "./components/sample9";
import { Sample10 } from "./components/sample10";
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
            <Link to="/1">1: 単純にノードを返すだけの例</Link>
          </li>
          <li>
            <Link to="/2">2: aタグでアクションを起こす例</Link>
          </li>
          <li>
            <Link to="/3">3: 簡単なログインフォーム</Link>
          </li>
          <li>
            <Link to="/4">
              4: function componentとclass componentでhistory.push
            </Link>
          </li>
          <li>
            <Link to="/5">5: contextの例</Link>
          </li>
          <li>
            <Link to="/6">6: useEffect</Link>
          </li>
          <li>
            <Link to="/7">7: contextの更新</Link>
          </li>
          <li>
            <Link to="/8">8: text inputと状態の同期</Link>
          </li>
          <li>
            <Link to="/9"> 9: contextとtext input</Link>
          </li>
          <li>
            <Link to="/10"> 10: formの中でボタンを使う</Link>
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
          <Route exact path="/7" component={Sample7} />
          <Route exact path="/8" component={Sample8} />
          <Route exact path="/9" component={Sample9} />
          <Route exact path="/10" component={Sample10} />
          <p>no match</p>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
