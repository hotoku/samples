import React, { useState, useContext } from "react";

type Font = {
  size: number;
  color: string;
};

const defaultFont: Font = {
  size: 16,
  color: "red",
};

export const FontContext = React.createContext({
  font: defaultFont,
  setValue: (v: Font) => {},
});

const Color = (props: {}) => {
  const { font, setValue } = useContext(FontContext);

  const updateColor = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue({
      ...font,
      color: e.target.value,
    });
  };

  return (
    <div>
      <form onSubmit={(e) => e.preventDefault()}>
        <input
          type="color"
          value={font.color}
          name="color"
          onChange={updateColor}
        />
      </form>
    </div>
  );
};

const Size = (props: {}) => {
  const { font, setValue } = useContext(FontContext);

  const updateSize = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue({
      ...font,
      size: parseFloat(e.target.value),
    });
  };

  return (
    <div>
      <form onSubmit={(e) => e.preventDefault()}>
        <input
          type="number"
          value={font.size}
          name="size"
          onChange={updateSize}
        />
      </form>
    </div>
  );
};

export const Sample11 = (props: {}) => {
  const [value, setValue] = useState(defaultFont);

  return (
    <div>
      <FontContext.Provider value={{ font: value, setValue: setValue }}>
        <Color />
        <Size />
        <h1 style={{ fontSize: `${value.size}px`, color: `${value.color}` }}>
          FONT SIZE {value.size}px
        </h1>
      </FontContext.Provider>
    </div>
  );
};
