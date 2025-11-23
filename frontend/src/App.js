import logo from './logo.svg';
import './App.css';

import List from "./components/List.js"

import { useEffect, useState } from "react";

function App() {
  
  // Stores dynamic data, causes re-render
  const [data, setData] = useState([]);
  const [currentSong, setCurrentSong] = useState(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [libraryStatus, setLibraryStatus] = useState(false);

  // Stores a reference/value, does not cause re-renders
  const audioRef = useRef(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000")
      .then((res) => res.json())
      // setData populates the data field
      .then((json) => setData(json))
      .catch((err) => console.error(err));
  }, []);

  // useEffect(() => { ... }, []) means only run this once after the component first loads, that's it
  if (!data) return <div>Loading...</div>;
  useEffect(() => {
    if (data.length > 0) setCurrentSong(data[0]);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <List items={data}/>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
