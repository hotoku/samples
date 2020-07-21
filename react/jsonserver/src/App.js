import React from "react";
import "./App.css";

class NameComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = { value: props.value };

    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    fetch("/todos")
      .then((res) => {
        console.log(res);
        return res.json();
      })
      .then(
        (result) => {
          this.setState({
            value: result[0].title,
          });
        },
        // 補足：コンポーネント内のバグによる例外を隠蔽しないためにも
        // catch()ブロックの代わりにここでエラーハンドリングすることが重要です
        (error) => {
          console.log(error);
        }
      );
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
