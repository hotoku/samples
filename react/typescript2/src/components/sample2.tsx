import React from "react";

interface IProps {
  cnt: number;
}

interface IState {
  count: number;
}

/*
   <a>のクリックで状態遷移する例
 */

export class Sample2 extends React.Component<IProps, IState> {
  state: IState;
  constructor(props: IProps) {
    super(props);
    this.state = { count: props.cnt };
  }

  handleClick = () => {
    this.setState({
      count: this.state.count + 1,
    });
  };

  render = () => {
    return (
      <div>
        <a href="#" onClick={this.handleClick}>
          increment
        </a>
        <p>{this.state.count}</p>
      </div>
    );
  };
}
