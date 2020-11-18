import React, { useContext } from "react";

import { AppContext } from "../sample5";

interface Props {}

export const C = (props: Props) => {
  const { x, y } = useContext(AppContext);
  return (
    <div>
      <ul>
        <li>C</li>
        <ul>
          <li>x={x}</li>
          <li>y={y}</li>
        </ul>
      </ul>
    </div>
  );
};
