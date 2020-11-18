import React from "react";

/* updateできるcontextの例
   https://www.carlrippon.com/react-context-with-typescript-p1/

   - 1. コンテキストの値の型を定義する
   - 2. コンテキストを定義
   - 3. Poroviderコンポーネントを定義
   -- 3.1 このコンポーネントの中でuseStateして状態と更新関数を作る
   -- 3.2 この状態と更新関数を、コンテキストの値とする
   - 4. コンテキストを取得するためのcustom hookを作る
   - 5. Providerの子孫コンテキストでコンテキストを取得し、値を使う or 更新する
 */

// 1
type ThemeContextType = {
  theme: string;
  setTheme: (value: string) => void;
};

// 2
const ThemeContext = React.createContext<ThemeContextType | undefined>(
  undefined
);

// 3
export const ThemeProvider = (props: { children: React.ReactNode }) => {
  // 3.1
  const [theme, setTheme] = React.useState();

  React.useEffect(() => {
    const currentTheme = "lightblue";
    setTheme(currentTheme);
  }, []);

  return (
    // 3.2
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {props.children}
    </ThemeContext.Provider>
  );
};

// 4.
export const useTheme = () => React.useContext(ThemeContext);

const Header = () => {
  // 5.
  const theme = useTheme();
  const val = theme ? theme.theme : "white";
  return (
    <div style={{ background: val }}>
      <button
        onClick={() => {
          if (theme) {
            theme.setTheme("black");
          }
        }}
      >
        black
      </button>
      <button
        onClick={() => {
          if (theme) {
            theme.setTheme("lightblue");
          }
        }}
      >
        blue
      </button>
    </div>
  );
};

export const Sample7 = () => {
  return (
    <ThemeProvider>
      <Header></Header>
    </ThemeProvider>
  );
};
