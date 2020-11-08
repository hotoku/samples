import React from "react";

import {
  Route,
  BrowserRouter,
  useHistory,
  Link,
  Switch,
  RouteComponentProps,
} from "react-router-dom";

function A() {
  const history = useHistory();
  return (
    <div>
      <p>A</p>
      <button
        onClick={(e) => {
          history.push("/4/A");
        }}
      >
        A
      </button>
      <button
        onClick={(e) => {
          history.push("/4/B");
        }}
      >
        B
      </button>
    </div>
  );
}

interface BProps extends RouteComponentProps<{}> {}

class B extends React.Component<BProps> {
  constructor(props: BProps) {
    super(props);
  }
  push = (s: string) => {
    this.props.history(s);
  };

  render = () => {
    return (
      <div>
        <p>B</p>
        <button
          onClick={(e) => {
            this.push("/4/A");
          }}
        >
          A
        </button>
        <button
          onClick={(e) => {
            this.push("/4/B");
          }}
        >
          B
        </button>
      </div>
    );
  };
}

function Default() {
  return (
    <div>
      <BrowserRouter>
        <ul>
          <li>
            <Link to="/4/A">A</Link>
          </li>
          <li>
            <Link to="/4/B">B</Link>
          </li>
        </ul>
        <Switch>
          <Route exact path="/4/A" component={A} />
          <Route exact path="/4/B" component={B} />
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export class Sample4 extends React.Component {
  render = () => {
    return (
      <div>
        <p>sample4</p>
        <Default />
      </div>
    );
  };
}
