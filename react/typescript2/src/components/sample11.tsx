import React, { useState } from "react";

interface Props {}

export const FontContext = React.createContext([0, (x: number) => {}]);

export const Sample11 = (props: Props) => {
  const [size, setSize] = useState(16);

  const _setSize = (size: number) => {
    setSize(size);
  };

  return (
    <div>
      <FontContext.Provider value={[size, _setSize]}>
        <h1 style={{ fontSize: `${size}px` }}>FONT SIZE {size}px</h1>
        <form onSubmit={(e) => e.preventDefault()}>
          <input
            type="number"
            value={size}
            onChange={(e) => setSize(parseFloat(e.target.value))}
          />
        </form>
      </FontContext.Provider>
    </div>
  );
};
