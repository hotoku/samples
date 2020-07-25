import React from "react";
import ReactDOM from "react-dom";
import { Map, TileLayer, Marker, Popup, Polygon } from "react-leaflet";
import "./index.css";

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
      <Map center={position} zoom={this.state.zoom}>
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
        <Map viewport={this.state.viewport}>
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

class App extends React.Component {
  render() {
    return (
      <div>
        <h1>SimpleExample</h1>
        <SimpleExample />
        <h1>PolygonExample</h1>
        <PolygonExample />
      </div>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("map-container"));
