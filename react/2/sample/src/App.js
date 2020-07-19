import React from "react";
import logo from "./logo.svg";
import { BrowserRouter, Link, Route, Switch } from "react-router-dom";

import "./App.css";

const Line = () => {
  return (
    <hr
      style={{
        color: "black",
        backgroundColor: "black",
        height: 1,
      }}
    />
  );
};

class App1 extends React.Component {
  render() {
    return (
      <div>
        <Line />
        <h1> {this.props.name}</h1>
      </div>
    );
  }
}

function App2(props) {
  return (
    <div>
      <Line />
      <h1> {props.name} </h1>
    </div>
  );
}

class App3 extends React.Component {
  render() {
    const users = [
      { name: "Tanaka", age: 26 },
      { name: "Suzuki", age: 32 },
      { name: "Yamada", age: 43 },
    ];
    const userList = users.map((user, index) => (
      <li key={index}>
        {user.name} (Age: {user.age})
      </li>
    ));
    return (
      <div>
        <Line />
        <ul>{userList}</ul>
      </div>
    );
  }
}

class App4 extends React.Component {
  constructor(props) {
    super(props);
    this.state = { cnt: 0 };
  }

  render() {
    return (
      <div>
        <Line />
        <h1>{this.state.cnt}</h1>
        <button onClick={() => this.setState({ cnt: this.state.cnt + 1 })}>
          Click
        </button>
      </div>
    );
  }
}

class App5 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [
        { name: "Tanaka", age: 26 },
        { name: "Suzuki", age: 32 },
      ],
    };
  }

  changeState() {
    let users = this.state.users;
    users.push({ name: "Yamada", age: 43 });
    this.setState({ users: users });
  }

  render() {
    let userList = this.state.users.map((user, index) => (
      <li key={index}>
        {user.name} (Age: {user.age})
      </li>
    ));
    return (
      <div>
        <Line />
        <ul>{userList}</ul>
        <button onClick={() => this.changeState()}>Click</button>
      </div>
    );
  }
}

function route1() {
  return <p>1</p>;
}

function route2() {
  return <p>2</p>;
}

class App6 extends React.Component {
  render() {
    return (
      <div>
        <Line />
        <BrowserRouter>
          <ul>
            <li>
              <Link to="/1">1</Link>
            </li>
            <li>
              <Link to="/2">2</Link>
            </li>
          </ul>
          <Route path="/1" component={route1} />
          <Route path="/2" component={route2} />
        </BrowserRouter>
      </div>
    );
  }
}

function routeA() {
  return <p>A</p>;
}

function routeB() {
  return <p>B</p>;
}

function routeX() {
  return <p>X</p>;
}

class App7 extends React.Component {
  render() {
    return (
      <div>
        <Line />
        <BrowserRouter>
          <ul>
            <li>
              <Link to="/">0</Link>
            </li>
            <li>
              <Link to="/1">1</Link>
            </li>
            <li>
              <Link to="/2">2</Link>
            </li>
          </ul>
          <Switch>
            <Route path="/1" component={routeA} />
            <Route path="/2" component={routeB} />
            <Route path="*" component={routeX} />
          </Switch>
        </BrowserRouter>
      </div>
    );
  }
}

class App8 extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      v: 0,
    };
  }
  render() {
    return (
      <div>
        <Line />
        <input
          id="app8_input"
          value={this.state.v}
          onChange={(e) => {
            const s = this.state;
            s.v = e.target.value;
            this.setState(s);
          }}
        />
        <p>{this.state.v}</p>
      </div>
    );
  }
}

function App() {
  return (
    <div>
      <App1 name="App1" />
      <App2 name="App2" />
      <App3 />
      <App4 />
      <App5 />
      <App6 />
      <App7 />
      <App8 />
    </div>
  );
}

export default App;
