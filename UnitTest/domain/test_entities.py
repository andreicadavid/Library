import unittest
from domain.entities import *

class TestBookGet(unittest.TestCase):
    def setUp(self):
        self.book = Book("15", "Title", "Description", "Author", 6)

    def test_id_get(self):
        self.assertTrue(self.book.get_id() == "15", "Book id should be 15")

    def test_title_get(self):
        self.assertTrue(self.book.get_title() == "Title", "Book tile should be Title")

    def test_description_get(self):
        self.assertTrue(self.book.get_description() == "Description", "Book description should be Description")

    def test_author_get(self):
        self.assertTrue(self.book.get_author() == "Author", "Book author should be Author")

    def test_brn_get(self):
        self.assertTrue(self.book.get_brn() == 6, "Book brn should be 6")

class TestBookSet(unittest.TestCase):
    def setUp(self):
        self.book = Book("15", "Title", "Description", "Author", 6)

    def test_id_set(self):
        self.book.set_id("77")
        self.assertTrue(self.book.get_id() == "77", "Book id should be 77")

    def test_title_set(self):
        self.book.set_title("Title2")
        self.assertTrue(self.book.get_title() == "Title2", "Book tile should be Title2")

    def test_description_set(self):
        self.book.set_description("Description2")
        self.assertTrue(self.book.get_description() == "Description2", "Book description should be Description2")

    def test_author_set(self):
        self.book.set_author("AuthorNew")
        self.assertTrue(self.book.get_author() == "AuthorNew", "Book author should be AuthorNew")

    def test_brn_set(self):
        self.book.set_brn(55)
        self.assertTrue(self.book.get_brn() == 55, "Book brn should be 55")

class TestBookStr(unittest.TestCase):
    def setUp(self):
        self.book = Book("15", "Title", "Description", "Author", 6)

    def test_str(self):
        self.assertTrue(str(self.book) == "id: 15   title: Title   description: Description   author: Author   rent: 6", "Book str should be 'id: 15   title: Title   description: Description   author: Author   rent: 6'")

class TestClientGet(unittest.TestCase):
    def setUp(self):
        self.client = Client("13", "Name", "5030326260056", [1, 2])

    def test_id_get(self):
        self.assertTrue(self.client.get_id() == "13", "Client id should be 13")

    def test_name_get(self):
        self.assertTrue(self.client.get_name() == "Name", "Client name should be Name")

    def test_cnp_get(self):
        self.assertTrue(self.client.get_cnp() == "5030326260056", "Client cnp should be 5030326260056")

    def test_list_rent_get(self):
        self.assertTrue(self.client.get_list_rent() == [1, 2], "Client list rent should be [1, 2]")

class TestClientSet(unittest.TestCase):
    def setUp(self):
        self.client = Client("13", "Name", "5030326260056", [1, 2])

    def test_id_set(self):
        self.client.set_id("55")
        self.assertTrue(self.client.get_id() == "55", "Client id should be 55")

    def test_name_set(self):
        self.client.set_name("NameNew")
        self.assertTrue(self.client.get_name() == "NameNew", "Client name should be NameNew")

    def test_cnp_set(self):
        self.client.set_cnp("5030326260055")
        self.assertTrue(self.client.get_cnp() == "5030326260055", "Client cnp should be 5030326260055")

    def test_list_rent_set(self):
        self.client.set_list_rent([1, 2, 3])
        self.assertTrue(self.client.get_list_rent() == [1, 2, 3], "Client list rent should be [1, 2, 3]")

class TestClientStr(unittest.TestCase):
    def setUp(self):
        self.client = Client("13", "Name", "5030326260056", [1, 2])

    def test_str(self):
        self.assertTrue(str(self.client) == "id: 13   name: Name   cnp: 5030326260056   RentedBooks: [1, 2]", "Client str should be 'id: 13   name: Name   cnp: 5030326260056   RentedBooks: [1, 2]'")

if __name__ == '__main__':
    unittest.main()