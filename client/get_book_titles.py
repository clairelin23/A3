

def get_book_titles(isbn_list, client):
    """
    Accept a client object as a parameter, which is then used to access RPC.
    Calls GetBook API.
    :param isbn_list: list of ISBN(s)
    :param client: client object from inventory_client.py
    :return: list of book titles that match with the list of ISBNs in the same order as the input list,
            the index position is '' if no matching book is found
    """
    client.start_server()
    found_titles = []
    for isbn in isbn_list:
        response = client.get_book(isbn)
        found_titles.append(response.title)
    return found_titles
