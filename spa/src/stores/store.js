import { EventEmitter } from "events";

class ListViewStore extends EventEmitter {
    changeEvent = 'ListViewStore.change'
    constructor(){
        super()
        this.list = ['あ','い','う']
    }

    getAll(){
        return this.list
    }

    append(){
        this.list.push('え')
        this.emit(this.changeEvent)
    }
}

const listViewStore = new ListViewStore();
export default listViewStore;