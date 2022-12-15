from __future__ import print_function

import logging
import grpc
import book_pb2
import book_pb2_grpc

"""
This client code is for calling the two APIs implements in server. 
The APIs can also be called/tested via Postman.
"""
def run():
    print("Will try to book inventory system ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.InventoryServiceStub(channel)
        # adding a book
        response = stub.CreateBook(book_pb2.CreateRequest(title="New Book",
                                                          ISBN="99999999",
                                                          genre="FICTION",
                                                          publishingYear=2022,
                                                          author="Claire Lin"))
        print("New book received: " + response.message)
        # looking for a book that exists
        response = stub.GetBook(book_pb2.GetRequest(ISBN="32843293"))
        print("New book received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
