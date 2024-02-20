class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books: list[Book] = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def search_books(self, search_string: str):
        return [ \
            self.books[i]
            for i in range(len(self.books))
            if search_string.lower() in self.books[i].title.lower()  \
            or search_string.lower() in self.books[i].author.lower() 
        ]
