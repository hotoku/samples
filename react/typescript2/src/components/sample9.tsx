import React from "react";

type ThemeContextType = {
  theme: string;
  setTheme: (value: string) => void;
};

const ThemeContext = React.createContext<ThemeContextType | undefined>(
  undefined
);

export const ThemeProvider = (props: { children: React.ReactNode }) => {
  const [theme, setTheme] = React.useState();

  React.useEffect(() => {
    const currentTheme = "lightblue";
    setTheme(currentTheme);
  }, []);

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {props.children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => React.useContext(ThemeContext);

const Header = () => {
  const theme = useTheme();
  const val = theme ? theme.theme : "white";

  return (
    <input
      type="text"
      value={val}
      onChange={(e) => {
        e.preventDefault(); // preventDefaultでイベントを抑制する
        if (theme) {
          theme.setTheme(e.target.value);
        }
        console.log(e.target.value);
      }}
    />
  );
};

export const Sample9 = () => {
  return (
    <ThemeProvider>
      <Header></Header>
    </ThemeProvider>
  );
};
