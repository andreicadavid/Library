from test.test_book import *
from test.test_book_repository import *
from test.test_book_service import *
from test.test_client import *
from test.test_client_repository import *
from test.test_client_service import *

def testAll():
    # functia apeleaza toate testele aplicatiei
    testBook_get()
    testBook_set()

    test_getAll_repository_book()
    test_getById_repository_book()
    test_addBook_repository_book()
    test_update_repository_book()
    test_delete_repository_book()

    test_getAll_service_book()
    test_addBook_service_book()
    test_update_service_book()
    test_delete_service_book()
    test_findById_service_book()
    test_rentBookById_service_book()
    test_rentBookSort_service_book()

    testClient_get()
    testClient_set()

    test_getAll_repository_client()
    test_getById_repository_client()
    test_addClient_repository_client()
    test_update_repository_client()
    test_delete_repository_client()

    test_getAll_service_client()
    test_addClient_service_client()
    test_update_service_client()
    test_delete_service_client()
    test_findById_service_client()
    test_rentBook_service_client()
    test_sortNameRentalNr_service_client()
    test_twenty_percent_service_client()