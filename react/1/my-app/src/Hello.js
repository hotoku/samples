import React from 'react';
import './App.css';

const msg = "Hello";


function Hello(props) {
  return (
    <h1 className="hello" style={{color:'red', fontSize:'20pt'}}>
      {msg} {props.name}!
    </h1>
  );
}


export default Hello;
