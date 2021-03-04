import React from 'react'
import listViewStore from '../stores/store'

class listView extends React.Component {

    constructor(props) {
        super(props);
        this.state = { 
            list: listViewStore.getAll()    
        };
    }
    render() {
        const { title, list} = this.state
        return (
        <div>
        <span>{title}</span><br/>
        <ul>
        { list.map(
            (element) => <li>{element}</li>
        )  }
        </ul>
        </div>
        )
    }

    componentDidMount(){
        listViewStore.on(listViewStore.change, ()=>{
            this.setState(
                {...this.state, list: listViewStore.getAll()}
            )
        })
    }

    componentWillUnmount(){
        listViewStore.removeAllListeners()
    }

}

export default listView;
