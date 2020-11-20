import React from "react";
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
import { Sample11 } from "./components/sample11";
import { Sample12 } from "./components/sample12";
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

const routes = [
  "単純にノードを返すだけの例",
  "aタグでアクションを起こす例",
  "簡単なログインフォーム",
  "function componentとclass componentでhistory.push",
  "contextの例",
  "useEffect",
  "contextの更新",
  "text inputと状態の同期",
  "contextとtext input",
  "formの中でボタンを使う",
  "オブジェクトのcontextを更新",
  "inputとstateの同期",
];

function App() {
  return (
    <div>
      <BrowserRouter>
        <ol>
          {routes.map((v, i) => {
            return (
              <li>
                <Link to={"/" + (i + 1)}>{v}</Link>
              </li>
            );
          })}
        </ol>
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
          <Route exact path="/11" component={Sample11} />
          <Route exact path="/12" component={Sample12} />
          <p>no match</p>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;
