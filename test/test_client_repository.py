from domain.entities import Client
from repository.client_repository import ClientRepository

# functiile testeaza repository-ul aplicatiei pentru client
def test_getAll_repository_client():
    clientRepository = ClientRepository()
    client = Client("13", "name", "5030326260056", [1, 2])
    clientRepository.addClient(client)

    clients = clientRepository.getAll()
    assert len(clients) == 1
    assert clients[0].get_id() == "13"

def test_getById_repository_client():
    clientRepository = ClientRepository()
    client = Client("13", "name", "5030326260056", [1, 2])
    clientRepository.addClient(client)

    client1 = clientRepository.getById(client.get_id())

    assert client1.get_id() == "13"
    assert client1.get_name() == "name"

def test_addClient_repository_client():
    clientRepository = ClientRepository()
    client = Client("13", "name", "5030326260056", [1, 2])
    clientRepository.addClient(client)

    clients = clientRepository.getAll()
    assert len(clients) == 1
    assert clients[0].get_id() == "13"

    try:
        clientRepository.addClient(client)
        assert False
    except KeyError:
        ...

def test_update_repository_client():
    clientRepository = ClientRepository()
    client1 = Client("13", "name1", "5030326260056", [1, 3])
    client2 = Client("13", "name2", "5030326260057", [1, 4])
    client3 = Client("166", "nam3", "5030326260058", [1, 5])
    clientRepository.addClient(client1)

    clientRepository.update(client2)

    clients = clientRepository.getAll()
    assert clients[0].get_name() == "name2"

    try:
        clientRepository.update(client3)
        assert False
    except KeyError:
        ...

def test_delete_repository_client():
    clientRepository = ClientRepository()
    client = Client("13", "name", "5030326260056", [1, 2])
    clientRepository.addClient(client)

    clientRepository.delete(client.get_id())

    clients = clientRepository.getAll()
    assert len(clients) == 0

    try:
        clientRepository.delete("423432")
        assert False
    except KeyError:
        ...