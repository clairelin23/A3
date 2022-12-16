import logging
from concurrent import futures
import grpc
import book_pb2
import book_pb2_grpc

from book_server import BookSystem

class Client:
    """
    Hide technical details of operating a server for API calls
    """
    def __init__(self, server_address, port_number):
        # set server address, port number
        self.server_address = server_address
        self.port_number = port_number
        logging.basicConfig()
        # set server settings
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        book_pb2_grpc.add_InventoryServiceServicer_to_server(BookSystem(), self.server)
        self.server.add_insecure_port('[::]:' + self.port_number)

    def start_server(self):
        """
        start the server
        :return: None
        """
        self.server.start()
        print("Server started, listening on " + self.port_number)

    def terminate_server(self):
        """
        shut down the server
        :return: None
        """
        self.server.stop(grace=None)

    def get_book(self, ISBN):
        """
        Wrapper function for calling the GetBook API
        :param ISBN: (string) ISBN of book
        :return: response as defined in book.proto
        """
        with grpc.insecure_channel(self.server_address + ':' + self.port_number) as channel:
            stub = book_pb2_grpc.InventoryServiceStub(channel)
            response = stub.GetBook(book_pb2.GetRequest(ISBN=ISBN))
            return response

    def add_book(self, ISBN, author, title, publishing_year, genre):
        """
        Wrapper function for calling the CreateBook API
        :param ISBN: (string) ISBN of book
        :param author: (string) author of book
        :param title: (string) title of book
        :param publishing_year: (int) publishing year of book
        :param genre: (string) genre of book
        :return: response as defined in book.proto
        """
        with grpc.insecure_channel('%s:%s' % self.server_address % self.server_address) as channel:
            stub = book_pb2_grpc.InventoryServiceStub(channel)
            response = stub.CreateBook(book_pb2.CreateRequest(title=title,
                                                              ISBN=ISBN,
                                                              genre=genre,
                                                              publishingYear=publishing_year,
                                                              author=author))
            return response
