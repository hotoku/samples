import * as _ from "lodash";
import "./style.css";
// @ts-ignore
import Data from "./data.xml";
// @ts-ignore
import Notes from "./data.csv";

import printMe from "./print";

function component() {
  const element = document.createElement("div");
  const btn = document.createElement("button");

  element.innerHTML = _.join(["Hello", "webpack", "!"], " ");
  element.classList.add("hello");

  btn.innerHTML = "Click";
  btn.onclick = printMe;

  element.appendChild(btn);

  console.log(Data);
  console.log(Notes);

  return element;
}

document.body.appendChild(component());
