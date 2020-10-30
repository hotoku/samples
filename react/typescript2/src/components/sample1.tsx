import React from "react";

interface IProps {
  name: string
}

export function Sample1(props: IProps) {
  return <div>{props.name}</div>
}


