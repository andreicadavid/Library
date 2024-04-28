import unittest
from domain.entities import Book
from repository.book_repository import BookRepository
from repository.client_repository import ClientRepository
from service.client_service import ClientService

class TestClientService(unittest.TestCase):
    def setUp(self):
        self.clientRepository = ClientRepository()
        self.bookRepository = BookRepository()
        self.clientService = ClientService(self.clientRepository, self.bookRepository)
        self.clientService.addClient("13", "Bogdan", "5030326260056", [1, 2])

    def test_getAll(self):
        clients = self.clientService.getAll()
        self.assertEqual(clients[0].get_cnp(), "5030326260056")

    def test_addClient(self):
        clients = self.clientService.getAll()
        self.assertEqual(clients[0].get_id(), "13")

        try:
            self.clientService.addClient("13", "Bogdan", "5030326260056", [1, 2])
            assert False
        except KeyError:
            assert True

    def test_update(self):
        self.clientService.update("13", "Alex", "5030326260058", [1, 2])
        clients = self.clientService.getAll()
        self.assertEqual(clients[0].get_name(), "Alex")
        self.assertEqual(clients[0].get_cnp(), "5030326260058")

        try:
            self.clientService.update("17", "Bogdan", "5030326260056", [1, 2])
            assert False
        except KeyError:
            assert True

    def test_delete(self):
        self.clientService.delete("13")
        clients = self.clientService.getAll()
        self.assertEqual(len(clients), 0)

        try:
            self.clientService.delete("67867")
            assert False
        except KeyError:
            assert True

    def test_findById(self):
        client = self.clientService.findById("13")
        self.assertEqual(client.get_id(), "13")
        client2 = self.clientService.findById("645")
        self.assertIsNone(client2)

    def test_rentBook(self):
        book = Book("15", "Title", "Description", "Author", 6)
        self.bookRepository.addBook(book)
        self.clientService.rentBook("15", "13")
        clients = self.clientService.getAll()
        self.assertEqual(clients[0].get_list_rent(), [1, 2, '15'])

        try:
            self.clientService.rentBook("15", "55")
            assert False
        except KeyError:
            assert True

    def test_sortNameRentalNr(self):
        self.clientService.addClient("14", "Alex", "5030326260057", [5, 6, 7, 8, 9, 10])
        self.clientService.addClient("15", "Sergiu", "5030326260058", [2, 5, 99, 100])
        self.clientService.addClient("16", "Paul", "5030326260059", [])
        sorted_list = self.clientService.sortNameRentalNr()
        self.assertEqual(len(sorted_list), 3)

        self.assertEqual(sorted_list[0].get_id(), "13")
        self.assertEqual(sorted_list[0].get_name(), "Bogdan")
        self.assertEqual(sorted_list[0].get_list_rent(), [1, 2])

        self.assertEqual(sorted_list[1].get_id(), "15")
        self.assertEqual(sorted_list[1].get_name(), "Sergiu")
        self.assertEqual(sorted_list[1].get_list_rent(), [2, 5, 99, 100])

        self.assertEqual(sorted_list[2].get_id(), "14")
        self.assertEqual(sorted_list[2].get_name(), "Alex")
        self.assertEqual(sorted_list[2].get_list_rent(), [5, 6, 7, 8, 9, 10])

    def test_twenty_percent(self):
        self.clientService.addClient("14", "Alex", "5030326260057", [5, 6, 7, 8, 9, 10])
        self.clientService.addClient("15", "Sergiu", "5030326260058", [2, 5, 99, 100])
        self.clientService.addClient("16", "Paul", "5030326260059", [])
        sorted_list = self.clientService.twenty_percent()

        self.assertEqual(len(sorted_list), 1)
        self.assertEqual(sorted_list[0].get_id(), "14")
        self.assertEqual(sorted_list[0].get_name(), "Alex")
        self.assertEqual(sorted_list[0].get_list_rent(), [5, 6, 7, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()