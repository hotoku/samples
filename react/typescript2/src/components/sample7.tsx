import React, { useState, useEffect } from "react";

/* updateできるcontextの例
   https://www.carlrippon.com/react-context-with-typescript-p1/
 */

const defaultTheme = "white";
const ThemeContext = React.createContext(defaultTheme);

/* Componetを定義
   このコンポーネントをrootとして、その下のコンポーネントでcontextが使えるようになる
 */
export const ThemeProvider = (props: { children: React.ReactNode }) => {
  const [theme, setTheme] = React.useState(defaultTheme);

  React.useEffect(() => {
    const currentTheme = "lightblue";
    setTheme(currentTheme);
  }, []);

  return (
    <ThemeContext.Provider value={theme}>
      {props.children}
    </ThemeContext.Provider>
  );
};

/* custom hookを定義
   子孫コンポーネントの中で使う。
 */
export const useTheme = () => React.useContext(ThemeContext);

/* contextの利用者
 */
const Header = () => {
  const theme = useTheme();
  // const theme = React.useContext(ThemeContext);
  // でも良い
  return <div style={{ background: theme }}>hello!</div>;
};

export const Sample7 = () => {
  return (
    <ThemeProvider>
      <Header></Header>
    </ThemeProvider>
  );
};
