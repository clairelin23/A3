from concurrent import futures
import logging

import grpc
import book_pb2
import book_pb2_grpc
from book import Book

"""
I am hard-coding 3 books (Book objects) and  putting them into a dictionary. 
This acts as the database of books on the server.
"""
book_dict = {}
book1 = Book("32843293", "Alice Wonderland", "Bob Wood", "FICTION", "1955")
book2 = Book("66666666", "Joy Luck Club", "Amy Shih", "ROMANCE", "2002")
book3 = Book("55555555", "Data Structures", "Calvin Smith", "FANTASY", "1990")
book_dict[book1.ISBN] = book1
book_dict[book2.ISBN] = book2
book_dict[book3.ISBN] = book3


class BookSystem(book_pb2_grpc.InventoryServiceServicer):
    """
    Implement the method CreateBook which adds a book given ISBN, title, author, genre, and publishing year
    """
    def CreateBook(self, request, context):
        new_book = Book(request.ISBN, request.title, request.author, request.genre, request.publishingYear)
        book_dict[new_book.ISBN] = new_book
        return book_pb2.CreateReply(message="successfully created book with ISBN: %s" % request.ISBN,
                                    title=request.title)

    """
    Implement the method GetBook which retrieves book details given an ISBN
    """
    def GetBook(self, request, context):
        found = book_dict.get(request.ISBN, None)
        if found:
            return book_pb2.GetReply(message="found book with ISBN: %s" % request.ISBN,
                                     title=found.title)
        else:
            return book_pb2.GetReply(message="CANNOT find book with ISBN: %s" % request.ISBN,
                                     title=None)


"""
Below code is for running the server from command line, only used in A3
"""


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_InventoryServiceServicer_to_server(BookSystem(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
