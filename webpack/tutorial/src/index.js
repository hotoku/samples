import * as _ from "lodash";
import "./style.css";
import Data from "./data.xml";
import Notes from "./data.csv";

function component() {
  const element = document.createElement("div");

  element.innerHTML = _.join(["Hello", "webpack", "!"], " ");
  element.classList.add("hello");

  console.log(Data);
  console.log(Notes);

  return element;
}

document.body.appendChild(component());
