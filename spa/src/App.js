import './App.css';
import React from 'react'
import ListView from './components/list'

class App extends React.Component {

  render() {
    return (
      <div className="App">
        <header className="App-header">
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
          <ListView title='mytitle'/>
        </header>
      </div>
    )
  }
}

export default App;
