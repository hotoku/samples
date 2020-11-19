import React, { useState, useContext } from "react";

type FontContextValue = {
  size: number;
  setSize: (size: number) => void;
};

const defaultFontContextValue: FontContextValue = {
  size: 16,
  setSize: (size: number) => {},
};

export const FontContext = React.createContext(defaultFontContextValue);

const Text = (props: {}) => {
  const { size, setSize } = useContext(FontContext);
  return (
    <div>
      <button onClick={() => setSize(size + 4)}>+4</button>
    </div>
  );
};

export const Sample11 = (props: {}) => {
  const [size, setSize] = useState(16);

  return (
    <div>
      <FontContext.Provider value={{ size, setSize }}>
        <form onSubmit={(e) => e.preventDefault()}>
          <Text />
          <input
            type="number"
            value={size}
            onChange={(e) => setSize(parseFloat(e.target.value))}
          />
        </form>
        <h1 style={{ fontSize: `${size}px` }}>FONT SIZE {size}px</h1>
      </FontContext.Provider>
    </div>
  );
};
