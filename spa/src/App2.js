import './App2.css';
import React from 'react'
import ListView from './components/list'
import AddButton from './components/pushbutton'


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
          <div className={this.state.sidebarOpen?"App-sidebar-container container-open":"App-sidebar-container"}>
            <div className={this.state.sidebarOpen?"App-sidebar sidebar-open":"App-sidebar"}/>
          </div>
          <div className="App-header">
            <button onClick={() => this.onSetSidebarOpen(true)}>
              Open sidebar
            </button>
          </div>
          <div className="App-content">
            <AddButton />
            <button>ああああ2</button>
            <ListView title='mytitle' />
          </div>
        </div>
      </div>
    )
  }
}

export default App;
