import React from 'react';
import './App.css';



function Hello(props) {
  const users = [
    { name: "Tanaka", age: 26 },
    { name: "Suzuki", age: 32 },
    { name: "Yamada", age: 43 }
  ];
  const userList = users.map(
    (user, index) =>
      <li key={index}>{user.name} (Age: {user.age})</li>
  );
  return (
    <ul>{userList}</ul>
  );
}


export default Hello;
