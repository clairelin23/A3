"""
The class for Book object
"""


class Book:
    def __init__(self, ISBN, title, author, genre, publishingYear):
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.genre = genre
        self.publishingYear = publishingYear
