import React from "react";

interface IProps {
  cnt: number
}

interface IState {
  count: number
}

export class Sample2 extends React.Component<IProps, IState> {
  state: IState;
  constructor(props: IProps) {
    super(props);
    this.state = { count: props.cnt };
  }

  handleClick = () => {
    // this.state.count = this.state.count + 1;
    // Do not mutate state directly という警告が出る
    this.setState({
      count: this.state.count + 1
    })
  }

  render = () => {
    return (
      <a href="#" onClick={this.handleClick}>{this.state.count}</a>
    );
  }
}
