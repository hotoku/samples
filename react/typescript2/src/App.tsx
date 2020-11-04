import React from "react";
import "./App.css";
import { Sample1 } from "./components/sample1";
import { Sample2 } from "./components/sample2";
import { Sample3 } from "./components/sample3";

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
      <Sample1 name="sample1" />
      <Line />
      <Sample2 cnt={0} />
      <Line />
      <Sample3 />
    </div>
  );
}

export default App;
