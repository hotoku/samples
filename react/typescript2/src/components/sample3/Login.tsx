import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import User from "./User";

interface Props {
  user: User;
  callback: (loggedin: boolean) => void;
}

export function Login(props: Props) {
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
            const ret = await props.user.login(password);
            props.callback(ret);
          })();
        }}
      >
        log in
      </button>
    </div>
  );
}
