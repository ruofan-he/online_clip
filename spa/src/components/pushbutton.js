import React from 'react'
import listViewStore from '../stores/store'

class AddButton extends React.Component {

    constructor(props) {
        super(props);
        this.state = {};
    }
    render() {
        return (<button onClick={listViewStore.append.bind(listViewStore)}>aasdfasd</button>)
    }
}
    
export default AddButton;
