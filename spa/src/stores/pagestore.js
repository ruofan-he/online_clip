import { EventEmitter } from "events";

class PageStore extends EventEmitter {
    event = {
        change: "change_page"
    }

    constructor(initialPage){
        super()
        this.page = initialPage

        this.get_page = this.get_page.bind(this)
        this.change_page = this.change_page.bind(this)
    }

    get_page(){
        return this.page
    }

    change_page(page){
        this.page = page
        this.emit(this.event.change)
    }
}

const pageStore = new PageStore('home');

export default pageStore;