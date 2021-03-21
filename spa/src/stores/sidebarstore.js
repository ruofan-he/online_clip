import { EventEmitter } from "events";

class SidebarStore extends EventEmitter {
    event = {
        chage: 'change'
    }

    constructor(){
        super()
        this._is_open = false
        this._is_docked = false

        this.is_open = this.is_open.bind(this)
        this.open = this.open.bind(this)
        this.close = this.close.bind(this)
        this.change = this.change.bind(this)
        this.is_docked = this.is_docked.bind(this)
        this.change_docked = this.change_docked.bind(this)
    }

    is_open(){
        return this._is_open
    }

    open(){
        this._is_open = true
        this.emit(this.event.change)
    }

    close(){
        this._is_open = false
        this.emit(this.event.change)
    }

    change(open){
        this._is_open = open
        this.emit(this.event.change)
    }

    is_docked(){
        return this._is_docked
    }

    change_docked(dock){
        this._is_docked = dock
        this._is_open = false
        this.emit(this.event.change)
    }
}

const sidebarStore = new SidebarStore();

export default sidebarStore;