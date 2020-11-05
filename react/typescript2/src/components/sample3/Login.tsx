import React, { useState } from "react";
import User from "./User";

export function Login(props: { user: User }) {
  const [password, setPassword] = useState("");

  return (
    <div>
      <label htmlFor="password">password</label>
      <input
        type="password"
        id="password"
        onChange={(e) => {
          setPassword(e.target.value);
        }}
      />
      <button
        value={password}
        onClick={(e) => {
          (async () => {
            await props.user.login(password);
          })();
        }}
      >
        log in
      </button>
    </div>
  );
}
