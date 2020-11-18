import React, { useState } from "react";

interface Props {}

/*
   この実装はうまく行かない
   ボタンを押すと更新されるが、すぐにcountが0に戻ってしまう
 */

export const Sample6 = (props: Props) => {
  const [count, setCount] = useState(0);

  return (
    <form>
      <button
        onClick={() => {
          setCount(count + 1);
        }}
      >
        increment
      </button>
      <p>count = {count}</p>
    </form>
  );
};
