import React, { useState } from "react";

export const Sample8 = () => {
  const [val, setVal] = useState("abc");

  return (
    <div>
      <input type="text" value={val}></input>{" "}
      <button
        onClick={() => {
          setVal(val + "a");
        }}
      >
        click
      </button>
    </div>
  );
};
