import React, { useState } from "react";

const MyContext = React.createContext({
  val: 0,
  setVal: (v: number) => {},
});

const Component1 = () => {
  const { val, setVal } = React.useContext(MyContext);
  return (
    <div>
      <h3>1</h3>
      <form onSubmit={(e) => e.preventDefault()}>
        <input
          value={val}
          type="number"
          step="1"
          onChange={(e) => setVal(parseFloat(e.target.value))}
        />
      </form>
    </div>
  );
};

const Component2 = () => {
  const { val, setVal } = React.useContext(MyContext);
  return (
    <div>
      <h3>2</h3>
      <form onSubmit={(e) => e.preventDefault()}>
        <input
          value={val}
          type="number"
          step="1"
          onChange={(e) => setVal(parseFloat(e.target.value))}
        />
      </form>
    </div>
  );
};

export const Sample13 = () => {
  const [val, setVal] = useState(100);
  return (
    <div>
      <MyContext.Provider value={{ val: val, setVal: setVal }}>
        <Component1 />
        <Component2 />
      </MyContext.Provider>
    </div>
  );
};
