import unittest
from unittest.mock import MagicMock, call

from get_book_titles import get_book_titles
from inventory_client import Client

"""
hard-coded parameters
"""
PORT_NUMBER = '50051'
SERVER_ADDR = 'localhost'
BOOKS = ['32843293', '66666666', '10101010']


class Testing(unittest.TestCase):

    def setUp(self) -> None:
        self.client = Client(port_number=PORT_NUMBER, server_address=SERVER_ADDR)

    def tearDown(self) -> None:
        self.client.terminate_server()

    def test_find_books_real_run(self):
        """
        real run test
        :return: None
        """
        # call function in get_book_titles.py
        found = get_book_titles(BOOKS, self.client)
        # assert that get_book() in inventory_client.py is called 3 times,
        # and the first two book was found, last one was not found (return '')
        self.assertEqual(found, ['Alice Wonderland', 'Joy Luck Club', ''])

    def test_find_books_mock(self):
        """
        testing client code without an actual server (calls to server is mocked)
        :return: None
        """
        # create mock client
        self.client.start_server = MagicMock()
        self.client.get_book = MagicMock()
        self.client.terminate_server = MagicMock()
        # call function in get_book_titles.py
        get_book_titles(BOOKS, self.client)
        # assert start_server() is called
        self.client.start_server.assert_called_with()
        # assert get_book() in inventory_client.py is called 3 times
        self.client.get_book.assert_has_calls([call(BOOKS[0]), call(BOOKS[1]), call(BOOKS[2])])
