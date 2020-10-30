import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [nRender, setNRender] = useState(0);
  const [count, setCount] = useState(0);
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
