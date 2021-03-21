import './App.css';
import React from 'react'
import pageStore from './stores/pagestore'
import Home from './pages/home'
import Setting from './pages/setting'
import Sidebar from './components/sidebar'
import { IoMdReorder } from "react-icons/io";
import sidebarStore from './stores/sidebarstore'
import { AiOutlineHome } from 'react-icons/ai';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      page: pageStore.get_page()
    }
  }

  componentDidMount() {
    pageStore.on(pageStore.event.change, () => {
      this.setState(
        { ...this.state, page: pageStore.get_page() }
      )
    })
  }

  componentWillUnmount() {
    pageStore.removeAllListeners()
  }

  render() {

    let content = null
    const { page } = this.state
    switch (page) {
      case 'home':
        content = <Home />
        break;
      case 'setting':
        content = <Setting />
      default:
        break;
    }

    return (
      <div className="App">
        <Sidebar />
        <div className="App-main">
          <div className="App-header">
            <button onClick={sidebarStore.open} style={{ margin: "0 1rem" }}>
              <IoMdReorder size={40} />
            </button>
            <button onClick={() => { pageStore.change_page('home') }}>
              <AiOutlineHome size="2rem" />
              <div style={{ width: "1rem" }} />
            </button>
          </div>
          <div className="App-content">
            {content}
          </div>
        </div>
      </div>
    )
  }
}

export default App;
