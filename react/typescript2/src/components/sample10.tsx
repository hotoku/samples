import React, { useState } from "react";

export function Sample10() {
  const [counter, setCounter] = useState(0);
  return (
    <div>
      <form>
        <button
          onClick={(e) => {
            e.preventDefault();
            // formタグの中でボタンを使う場合、
            // preventDefaultがないと、ブラウザのリロードが走り、状態が初期化されてしまう。
            setCounter(counter + 1);
          }}
        >
          click
        </button>
      </form>
      <p>count={counter}</p>
    </div>
  );
}
