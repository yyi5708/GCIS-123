#

class Book:

    __slots__ = ["title", "author", "copies"]

    def __init__(self, title, author, copies):

        (self.title) = (title)
        (self.author) = (author)
        (self.copies) = (copies)

class Patron:

    __slots__ = ["id", "name", "want_list", "checked_out_books"]

    def __init__(self, id, name):

        (self.id) = (id)
        (self.name) = (name)
        (self.want_list) = (set())
        (self.checked_out_books) = (set())

class CardCatalog:

    __slots__ = ["books_by_author", "books_by_title"]

    def __init__(self):

        (self.books_by_author) = (dict())
        (self.books_by_title) = (dict())

class Library:

    __slots__ = ["card_catalog", "patrons", "shelves"]

    def __init__(self):

        (self.card_catalog) = (CardCatalog())
        (self.patrons) = (dict())
        (self.shelves) = (set())