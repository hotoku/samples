import React from "react";
import { A } from "./sample5/A";

interface Props {}

export const AppContext = React.createContext({
  x: 1,
  y: "abc",
});

export const Sample5 = (props: Props) => {
  return (
    <AppContext.Provider value={{ x: 10, y: "xyz" }}>
      <A />
    </AppContext.Provider>
  );
};
