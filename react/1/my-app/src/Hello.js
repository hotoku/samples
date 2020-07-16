import React from 'react';
import './App.css';

const msg = "Hello";


function Hello(props) {
  return (
    <div>
      <h1 className="hello" style={{color:'red', fontSize:'20pt'}}>
        {msg} {props.name}!
      </h1>
      <button onClick={(e) => {
        console.log("click", this);
        console.log(e, this);
      }}>
        OK
      </button>
    </div>
  );
}


export default Hello;
