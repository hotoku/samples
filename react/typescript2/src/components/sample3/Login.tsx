import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import User from "./User";

export function Login(props: { user: User }) {
  const [password, setPassword] = useState("");
  const history = useHistory();

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
            history.push("/3");
          })();
        }}
      >
        log in
      </button>
    </div>
  );
}
