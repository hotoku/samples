import React, { useState } from "react";
import { useHistory } from "react-router-dom";
import User from "./User";

export function Logout(props: { user: User }) {
  const history = useHistory();
  props.user.logout();
  history.push("/3");

  return null;
}
