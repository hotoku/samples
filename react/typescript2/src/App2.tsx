import React, { useState } from "react";
import "./App.css";

function App() {
  const [counter, setCounter] = useState(0);
  return (
    <div>
      <p>
        <button onClick={() => setCounter(counter + 1)}>click</button>
      </p>
      <p>count={counter}</p>
    </div>
  );
}

export default App;
