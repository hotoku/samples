import React from 'react';
import './App.css';

const msg = "Hello"


function Hello(props) {
  return <h1>{msg} {props.name}!</h1>;
}


export default Hello;
