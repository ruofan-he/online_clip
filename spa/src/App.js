import './App.css';
import React from 'react'
import ListView from './components/list'
import AddButton from './components/pushbutton'
import Sidebar from "react-sidebar";


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      sidebarOpen: false
    };
    this.onSetSidebarOpen = this.onSetSidebarOpen.bind(this);
  }

  onSetSidebarOpen(open) {
    // this.setState({ sidebarOpen: open });
    this.setState({sidebarOpen: !this.state.sidebarOpen})
  }

  render() {

    return (
      <div className="App">
        <div className="App-main">
          <div className="App-sidebar-container">
            <div className={this.state.sidebarOpen?"App-sidebar sidebar-open":"App-sidebar"}/>
          </div>
          <div className="App-header">
            <button onClick={() => this.onSetSidebarOpen(true)}>
              Open sidebar
            </button>
          </div>
          <div className="App-content">
            <AddButton />
            <ListView title='mytitle' />
          </div>
        </div>
      </div>
    )
  }
}

export default App;
