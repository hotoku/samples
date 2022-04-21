import React, { useState, useEffect } from "react";

export const Sample15 = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <div>
        <button
          onClick={() => {
            // これだと、setCountを2回、呼び出しても、countは1しか増えない
            setCount(count + 1);
            setCount(count + 1);
          }}
        >
          +1
        </button>{" "}
        <button
          onClick={() => {
            // useStateのsetterは、値を直接渡すのではなく更新関数を渡す
            setCount((c) => c + 1);
            setCount((c) => c + 1);
          }}
        >
          +2
        </button>
        <p>{count}</p>
      </div>
    </div>
  );
};
