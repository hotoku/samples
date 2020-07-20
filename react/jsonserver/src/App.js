import React from "react";
import "./App.css";

class NameComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: props.value };

    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    const updateValue = () => {
      const v = this.state;
      v.value = this.state.value + "x";
      this.setState(v);
      setTimeout(updateValue, 1000);
    };
    setTimeout(updateValue, 1000);
  }

  handleChange(event) {
    this.setState({ value: event.target.value });
  }

  render() {
    return (
      <form>
        <label>
          Name:
          <input
            type="text"
            value={this.state.value}
            onChange={this.handleChange}
          />
        </label>
      </form>
    );
  }
}

function App() {
  return <NameComponent value="horikoshi" />;
}

export default App;
