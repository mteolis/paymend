import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";

const axios = require("axios").default;

function App() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    axios.get("/time").then(function (response) {
      console.log(response);
      setCurrentTime(response.data.time);
      console.log(response.data.neep);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        {currentTime !== 0 && <p>The current time is {currentTime}.</p>}
      </header>
    </div>
  );
}

export default App;
