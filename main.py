from UnitTest.repository.test_book_repository import TestBookRepository
from UnitTest.repository.test_client_repository import TestClientRepository
from UnitTest.service.test_book_service import TestBookService
from UnitTest.service.test_client_service import TestClientService
from repository.book_file_repository import BookFileRepository
from repository.client_file_repository import ClientFileRepository
from service.client_service_reports import ReportsService
from ui.console import Console
from test.test_all import *
from UnitTest.domain.test_entities import *

def run_some_tests():
    # Run only the tests in the specified classes

    test_classes_to_run = [TestBookGet, TestBookSet, TestClientGet, TestClientSet, TestBookStr, TestClientStr, TestBookRepository, TestClientRepository, TestBookService, TestClientService]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)

def main():
    # functia main apeleaza toate functiile aplicatiei
    #testAll()

    run_some_tests()
    #bookRepository = BookRepository()
    bookRepository = BookFileRepository("books.txt")
    #clientRepository = ClientRepository()
    clientRepository = ClientFileRepository("clients.txt")
    bookService = BookService(bookRepository)
    clientService = ClientService(clientRepository, bookRepository)
    reportsService = ReportsService(clientRepository, bookRepository)
    console = Console(bookService, clientService, reportsService)
    console.Menu()

main()