from repository.book_repository import BookRepository
from service.book_service import BookService

# functiile testeaza service-ul aplicatiei pentru carte
def test_getAll_service_book():
    bookRepository = BookRepository()
    bookService = BookService(bookRepository)
    bookService.addBook("15", "Title", "Description", "Author", 6)
    bookService.addBook("16", "Title2", "Description", "Author", 6)

    books = bookService.getAll()
    assert len(books) == 2
    assert books[0].get_id() == "15"
    assert books[1].get_id() == "16"

def test_addBook_service_book():
    bookRepository = BookRepository()
    bookService = BookService(bookRepository)
    bookService.addBook("15", "Title", "Description", "Author", 6)

    books = bookService.getAll()
    assert len(books) == 1
    assert books[0].get_id() == "15"

    try:
        bookService.addBook("15", "Title", "Description", "Author", 6)
        assert False
    except KeyError:
        ...

def test_update_service_book():
    bookRepository = BookRepository()
    bookService = BookService(bookRepository)
    bookService.addBook("15", "Title", "Description", "Author", 6)

    bookService.update("15", "Title2", "Description2", "Author2", 6)

    books = bookService.getAll()
    assert len(books) == 1
    assert books[0].get_title() == "Title2"

    try:
        bookService.update("17", "Title2", "Description2", "Author2", 6)
        assert False
    except KeyError:
        ...

def test_delete_service_book():
    bookRepository = BookRepository()
    bookService = BookService(bookRepository)
    bookService.addBook("15", "Title", "Description", "Author", 6)

    bookService.delete("15")

    books = bookService.getAll()
    assert len(books) == 0

    try:
        bookService.delete("234234")
        assert False
    except KeyError:
        ...

def test_findById_service_book():
    bookRepository = BookRepository()
    bookService = BookService(bookRepository)
    bookService.addBook("15", "Title", "Description", "Author", 6)

    book = bookService.findById("15")
    assert book.get_id() == "15"
    assert book.get_title() == "Title"

    book2 = bookService.findById("1444")
    assert book2 == None

def test_rentBookById_service_book():
    bookRepository = BookRepository()
    bookService = BookService(bookRepository)
    bookService.addBook("15", "Title", "Description", "Author", 6)

    bookService.rentBookById("15")
    books = bookService.getAll()
    assert books[0].get_brn() == 7

    try:
        bookService.rentBookById("534")
        assert False
    except KeyError:
        ...

def test_rentBookSort_service_book():
    bookRepository = BookRepository()
    bookService = BookService(bookRepository)
    bookService.addBook("15", "Title1", "Description1", "Author1", 1)
    bookService.addBook("16", "Title2", "Description2", "Author2", 10)
    bookService.addBook("17", "Title3", "Description3", "Author3", 7)

    bookService.rentBookSort()
    books = bookService.getAll()

    assert len(books) == 3
    assert books[0].get_id() == "16"
    assert books[1].get_id() == "17"
    assert books[2].get_id() == "15"

    assert books[0].get_title() == "Title2"
    assert books[1].get_title() == "Title3"
    assert books[2].get_title() == "Title1"

    assert books[0].get_description() == "Description2"
    assert books[1].get_description() == "Description3"
    assert books[2].get_description() == "Description1"

    assert books[0].get_author() == "Author2"
    assert books[1].get_author() == "Author3"
    assert books[2].get_author() == "Author1"

    assert books[0].get_brn() == 10
    assert books[1].get_brn() == 7
    assert books[2].get_brn() == 1