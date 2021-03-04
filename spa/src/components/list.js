import React from 'react'

class listView extends React.Component {

    constructor(props) {
        super(props);
        this.state = { title: props.title };
    }
    render() {
        return (<div>{this.state.title}</div>)
    }
}

export default listView;
