import React from "react";
import { A } from "./sample5/A";
import { B } from "./sample5/B";
import { C } from "./sample5/C";

interface Props {}

/* contextの利用例 */

export const AppContext = React.createContext({
  x: 1,
  y: "abc",
});

export const Sample5 = (props: Props) => {
  return (
    <AppContext.Provider value={{ x: 10, y: "xyz" }}>
      <p>contextの例</p>
      <A />
      <B />
    </AppContext.Provider>
  );
};
