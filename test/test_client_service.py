from domain.entities import Book
from repository.client_repository import ClientRepository
from repository.book_repository import BookRepository
from service.client_service import ClientService

# functiile testeaza service-ul aplicatiei pentru client
def test_getAll_service_client():
    clientRepository = ClientRepository()
    bookRepository = BookRepository()
    clientService = ClientService(clientRepository, bookRepository)
    clientService.addClient("13", "name", "5030326260056", [1, 2])

    clients = clientService.getAll()
    assert len(clients) == 1
    assert clients[0].get_cnp() == "5030326260056"

def test_addClient_service_client():
    clientRepository = ClientRepository()
    bookRepository = BookRepository()
    clientService = ClientService(clientRepository, bookRepository)
    clientService.addClient("13", "name", "5030326260056", [1, 2])

    clients = clientService.getAll()
    assert len(clients) == 1
    assert clients[0].get_id() == "13"

    try:
        clientService.addClient("13", "name", "5030326260056", [1, 2])
        assert False
    except KeyError:
        ...

def test_update_service_client():
    clientRepository = ClientRepository()
    bookRepository = BookRepository()
    clientService = ClientService(clientRepository, bookRepository)
    clientService.addClient("13", "name", "5030326260056", [1, 2])

    clientService.update("13", "name1", "5030326260056", [1, 2])

    clients = clientService.getAll()
    assert len(clients) == 1
    assert clients[0].get_name() == "name1"

    try:
        clientService.update("15", "name1", "5030326260056", [1, 2])
        assert False
    except KeyError:
        ...

def test_delete_service_client():
    clientRepository = ClientRepository()
    bookRepository = BookRepository()
    clientService = ClientService(clientRepository, bookRepository)
    clientService.addClient("13", "name", "5030326260056", [1, 2])

    clientService.delete("13")

    clients = clientService.getAll()
    assert len(clients) == 0

    try:
        clientService.delete("31231")
        assert False
    except KeyError:
        ...

def test_findById_service_client():
    clientRepository = ClientRepository()
    bookRepository = BookRepository()
    clientService = ClientService(clientRepository, bookRepository)
    clientService.addClient("13", "name", "5030326260056", [1, 2])

    client = clientService.findById("13")
    assert client.get_id() == "13"

    client2 = clientService.findById("131231")
    assert client2 == None

def test_rentBook_service_client():
    clientRepository = ClientRepository()
    bookRepository = BookRepository()
    clientService = ClientService(clientRepository, bookRepository)
    clientService.addClient("13", "name", "5030326260056", [1, 2])
    book = Book("15", "Title", "Description", "Author", 6)
    bookRepository.addBook(book)

    clientService.rentBook("15", "13")

    clients = clientService.getAll()
    assert clients[0].get_list_rent() == [1, 2, '15']

    try:
        clientService.rentBook("15", "20")
        assert False
    except KeyError:
        ...

def test_sortNameRentalNr_service_client():
    clientRepository = ClientRepository()
    bookRepository = BookRepository()
    clientService = ClientService(clientRepository, bookRepository)
    clientService.addClient("13", "Bogdan", "5030326260056", [1, 2, 3])
    clientService.addClient("14", "Alex", "5030326260057", [5, 6, 7, 8, 9, 10])
    clientService.addClient("15", "Sergiu", "5030326260058", [2, 5, 99, 100])
    clientService.addClient("16", "name4", "5030326260059", [])

    sorted_list = clientService.sortNameRentalNr()

    assert len(sorted_list) == 3
    assert sorted_list[0].get_id() == "13"
    assert sorted_list[0].get_name() == "Bogdan"
    assert sorted_list[0].get_list_rent() == [1, 2, 3]

    assert sorted_list[1].get_id() == "15"
    assert sorted_list[1].get_name() == "Sergiu"
    assert sorted_list[1].get_list_rent() == [2, 5, 99, 100]

    assert sorted_list[2].get_id() == "14"
    assert sorted_list[2].get_name() == "Alex"
    assert sorted_list[2].get_list_rent() == [5, 6, 7, 8, 9, 10]

def test_twenty_percent_service_client():
    clientRepository = ClientRepository()
    bookRepository = BookRepository()
    clientService = ClientService(clientRepository, bookRepository)
    clientService.addClient("13", "Bogdan", "5030326260056", [1, 2, 3])
    clientService.addClient("14", "Alex", "5030326260057", [5, 6, 7, 8, 9, 10])
    clientService.addClient("15", "Sergiu", "5030326260058", [2, 5, 99, 100])
    clientService.addClient("16", "name4", "5030326260059", [])

    sorted_list = clientService.twenty_percent()

    assert len(sorted_list) == 1
    assert sorted_list[0].get_id() == "14"
    assert sorted_list[0].get_name() == "Alex"
    assert sorted_list[0].get_list_rent() == [5, 6, 7, 8, 9, 10]