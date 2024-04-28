import unittest
from repository.client_repository import ClientRepository
from domain.entities import Client

class TestClientRepository(unittest.TestCase):
    def setUp(self):
        self.clientRepository = ClientRepository()
        self.client = Client("13", "name", "5030326260056", [1, 2])
        self.clientRepository.addClient(self.client)

    def test_getAll(self):
        clients = self.clientRepository.getAll()
        self.assertEqual(clients[0].get_id(), "13")

    def test_getById(self):
        client = self.clientRepository.getById(self.client.get_id())
        self.assertEqual(client.get_name(), "name")

    def test_addClient(self):
        client = Client("11", "Bogdan", "5030326260057", [1, 2, 3])
        self.clientRepository.addClient(client)
        clients = self.clientRepository.getAll()
        self.assertEqual(clients[1].get_id(), "11")

        try:
            self.clientRepository.addClient(self.client)
            assert False
        except KeyError:
            assert True

    def test_update(self):
        client = Client("13", "Bogdan", "5030326260057", [1, 2, 3])
        self.clientRepository.update(client)
        clients = self.clientRepository.getAll()
        self.assertEqual(clients[0].get_name(), "Bogdan")

        try:
            client_new = Client("17", "Bogdan", "5030326260057", [1, 2, 3])
            self.clientRepository.update(client_new)
            assert False
        except KeyError:
            assert True

    def test_delete(self):
        self.clientRepository.delete(self.client.get_id())
        clients = self.clientRepository.getAll()
        self.assertEqual(len(clients), 0)

        try:
            self.clientRepository.delete("32423")
            assert False
        except KeyError:
            assert True

if __name__ == '__main__':
    unittest.main()