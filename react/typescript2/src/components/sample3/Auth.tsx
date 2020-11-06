import React, { FC } from "react";
import { Redirect } from "react-router-dom";
import User from "./User";

type Props = {
  user: User;
};

const Auth: FC<Props> = ({ user, children }) => {
  return <div>{user.loggedin ? children : <Redirect to="/3/login" />}</div>;
};

export default Auth;
