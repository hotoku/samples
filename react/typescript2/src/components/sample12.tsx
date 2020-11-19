import React from "react";

export const Sample12 = (props: {}) => {
  const [state, setState] = React.useState("a");
  return (
    <div>
      <form onSubmit={(e) => e.preventDefault()}>
        <input
          type="text"
          value={state}
          onChange={(e) => {
            setState(e.target.value);
          }}
        />{" "}
      </form>
    </div>
  );
};
