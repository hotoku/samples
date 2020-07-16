import React from "react";
import "./App.css";

class Hello extends React.Component {
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
        <ul>{userList}</ul>
        <button onClick={() => this.changeState()}>Click</button>
      </div>
    );
  }
}

export default Hello;
