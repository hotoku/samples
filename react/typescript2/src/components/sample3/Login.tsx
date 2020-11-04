import React, { useState } from "react";
import User from "./User";

export function Login(props: { user: User }) {
  const [password, setPassword] = useState("");

  return (
    <div>
      <label htmlFor="password">password</label>
      <input
        type="text"
        id="password"
        onChange={(e) => {
          setPassword(e.target.value);
        }}
      />
      <button
        value={password}
        onClick={(e) => {
          console.log(props.user);
          props.user.login(password);
        }}
      >
        log in
      </button>
    </div>
  );
}
