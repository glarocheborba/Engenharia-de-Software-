class Book {
    constructor(title, description, author, id) {
    this.title = title
    this.description = description
    this.author = author
    this.id = id
    }
}


class Library {
    constructor() {
        this.books = []
    }

    addBook(bookInfo) {
        let newBook = new Book(bookInfo['title'], bookInfo['description'], bookInfo['author'])
        this.books.push(newBook)

        return newBook
    }

    getBooks() {
        return this.books
    }

    removeBookById(id) {
        let cond = 1;
        for (let i = 0; i < this.books.length; i++) {
            if (this.books[i]['id'] === id) {
                this.books.splice(i, 1);
                cond = 2;
                break
            } 
        }
        if (cond === 1) {
            console.log('Not found book')
        }
    }

    getBookById(id) {
        let cond = 1;
        for (let i = 0; i < this.books.length; i++) {
            if (this.books[i]['id'] === id) {
                cond = 2;
                return this.books[i]
            } 
        }
        if (cond === 1) {
            console.log('Not found book')
        }
    }

    updateBookById(id, info) {
        let cond = 1;
        for (let i = 0; i < this.books.length; i++) {
            if (this.books[i]['id'] === id) {
                this.books[i]['title'] = info['title'];
                this.books[i]['description'] = info['description'];
                this.books[i]['author'] = info['author'];
                
                cond = 2;
                return this.books[i]
            }
        } 
        if (cond === 1) {
            console.log('Livro não encontrado')
        }
    }
}
