import React from "react";
import ReactDOM from "react-dom";
import { Map, TileLayer, Marker, Popup, Polygon } from "react-leaflet";
import "./index.css";

const style = {
  height: "200px",
  width: "95%",
};

class SimpleExample extends React.Component {
  constructor() {
    super();
    this.state = {
      lat: 51.505,
      lng: -0.09,
      zoom: 13,
    };
  }

  render() {
    const position = [this.state.lat, this.state.lng];
    return (
      <div>
        <Map center={position} zoom={this.state.zoom} style={style}>
          <TileLayer
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
          />
          <Marker position={position}>
            <Popup>
              A pretty CSS3 popup. <br /> Easily customizable.
            </Popup>
          </Marker>
        </Map>
      </div>
    );
  }
}

class PolygonExample extends React.Component {
  constructor() {
    super();
    this.state = {
      viewport: {
        center: [51.505, -0.09],
        zoom: 13,
      },
    };
  }
  render() {
    const pos = [
      [51.505, -0.085],
      [51.51, -0.085],
      [51.51, -0.09],
      [51.505, -0.09],
    ];

    return (
      <div>
        <Map viewport={this.state.viewport} style={style}>
          <TileLayer
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
          />
          <Polygon color="red" positions={pos} />
        </Map>
      </div>
    );
  }
}

class PopupExample extends React.Component {
  constructor() {
    super();
    this.state = {
      viewport: {
        center: [51.505, -0.09],
        zoom: 13,
      },
    };
  }
  render() {
    const pos = [51.505, -0.085];
    return (
      <div>
        <Map viewport={this.state.viewport} style={style}>
          <TileLayer
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
          />
          <Popup position={pos}>aaa</Popup>
        </Map>
      </div>
    );
  }
}

class OnclickExample extends React.Component {
  constructor() {
    super();
    this.state = {
      viewport: {
        center: [51.505, -0.09],
        zoom: 13,
      },
      popPos: null,
    };
  }

  handleClick = (e) => {
    this.setState({
      popPos: this.state.viewport.center,
    });
  };

  popup = () => {
    if (this.state.popPos) {
      return (
        <Popup
          position={this.state.popPos}
          onClose={() => {
            /*
              状態が変化しないと再描画されない。1度消えたあと、再度クリックされたときに
              描画されるようにするため、stateをクリアしておく
            */
            this.setState({ popPos: null });
          }}
        >
          click!
        </Popup>
      );
    } else {
      return <div />;
    }
  };

  render() {
    return (
      <div>
        <Map
          viewport={this.state.viewport}
          onClick={this.handleClick}
          style={style}
        >
          <TileLayer
            attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
            url="https://{s}.tile.osm.org/{z}/{x}/{y}.png"
          />
          {this.popup()}
        </Map>
      </div>
    );
  }
}

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>SimpleExample</h1>
        <SimpleExample />
        <h1>PolygonExample</h1>
        <PolygonExample />
        <h1>PopupExample</h1>
        <PopupExample />
        <h1>OnclickExample</h1>
        <OnclickExample />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("map-container"));
