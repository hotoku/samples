import React from "react";

import { AppContext } from "../sample5";

interface Props {}

export const A = (props: Props) => {
  return (
    <AppContext.Consumer>
      {({ x, y }) => {
        return (
          <div>
            <ul>
              <li>A</li>
              <ul>
                <li>x={x}</li>
                <li>y={y}</li>
              </ul>
            </ul>
          </div>
        );
      }}
    </AppContext.Consumer>
  );
};
