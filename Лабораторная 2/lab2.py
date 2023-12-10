class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f'Книга {self.name}'

    def __repr__(self):
        return f'Book(id_={self.id}, name={self.name}, pages={self.pages})'


class Library:
    def __init__(self, books = None):
        self.books = books or []

    def get_next_book_id(self):
        if not self.books:
            return 1
        return self.books[-1].id_ + 1

    def get_index_by(self, book_id):
        for index, book in enumerate(self.books):
            if book.id_ == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")
