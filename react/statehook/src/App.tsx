import React, { useState } from 'react';
import './App.css';


function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <header className="App-header">
        <div>
          <p>
            count = {count}
          </p>
          <button onClick={() => setCount(count + 1)}>click</button>
        </div>
      </header>
    </div>
  );
}

export default App;
