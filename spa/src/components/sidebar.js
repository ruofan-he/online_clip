import './sidebar.css'
import React from "react";
import Sidebar from "react-sidebar";
import sidebarStore from '../stores/sidebarstore';
import pageStore from '../stores/pagestore';
import { AiOutlineHome } from 'react-icons/ai';
import { FiSettings, FiChevronsRight, FiChevronsLeft } from 'react-icons/fi';




class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      is_open: false,
      is_docked: false
    };

    this.onSidebarChange = this.onSidebarChange.bind(this);
  }

  createList() {
    return (
      <div className='sidebar-content' >
        <button className='sidebar-element' onClick={()=>{sidebarStore.change_docked(false)}}>
          <FiChevronsLeft size="2rem"/>
        </button>
        <button className='sidebar-element' onClick={() => { pageStore.change_page('home') }}>
          <AiOutlineHome size="2rem" />
          <div style={{ width: "1rem" }} />
          <span>{"ホーム"}</span>
        </button>
        <button className='sidebar-element' onClick={() => { pageStore.change_page('setting') }}>
          <FiSettings size="2rem" />
          <div style={{ width: "1rem" }} />
          <span>{"セッティング"}</span>
        </button>
      </div>
    )
  }

  onSidebarChange() {
    this.setState({ ...this.state, is_open: sidebarStore.is_open(), is_docked: sidebarStore.is_docked() });
  }

  componentDidMount() {
    sidebarStore.on(sidebarStore.event.change, this.onSidebarChange)
  }

  componentWillUnmount() {
    sidebarStore.removeAllListeners()
  }

  render() {
    const { is_open, is_docked } = this.state
    const sidebarStyle = {
      width: "20rem",
      background: "white"
    }

    return (
      <Sidebar
        sidebar={this.createList()}
        open={is_open}
        onSetOpen={sidebarStore.change}
        styles={{ sidebar: sidebarStyle }}
        docked={is_docked}
      >
        {is_docked || <button onClick={ ()=>{sidebarStore.change_docked(true)}} style={{padding: "1rem"}}><FiChevronsRight size="2rem" /></button>}
      </Sidebar>
    );
  }
}

export default App;