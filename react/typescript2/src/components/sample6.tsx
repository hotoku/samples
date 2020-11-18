import React, { useState, useEffect } from "react";

interface Props {}

export const Sample6 = (props: Props) => {
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log("effect: count=", count);
  });
  /* as far as i understand ..
     直接、関数の中に副作用を書くと、ボタンを押すごとに一回、ではなく
     複数回、呼ばれてしまう。
     実際に描画されるタイミング以外にも、ツリーを計算するタイミングがある為と思われる
   */
  console.log("function: count=", count);

  return (
    <div>
      <button
        onClick={() => {
          setCount(count + 1);
        }}
      >
        increment
      </button>
      <p>count = {count}</p>
    </div>
  );
};
