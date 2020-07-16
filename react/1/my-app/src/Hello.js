import React from 'react';
import './App.css';

class Hello extends React.Component {
  constructor(props) {
    super(props);
    this.state = { msg: 'Hello!' };
  }

  render() {
    return (
      <div>
        <h1>{this.state.msg}</h1>
        <button onClick={() => this.setState({msg: 'Bye!'})}>Click</button>
      </div>
    );
  }
}


export default Hello;
