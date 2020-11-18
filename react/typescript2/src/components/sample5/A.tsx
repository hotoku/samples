import React from "react";

import { AppContext } from "../sample5";

interface Props {}

export const A = (props: Props) => {
  return (
    <AppContext.Consumer>
      {({ x, y }) => {
        return (
          <div>
            <p>x={x}</p>
            <p>y={y}</p>
          </div>
        );
      }}
    </AppContext.Consumer>
  );
};
