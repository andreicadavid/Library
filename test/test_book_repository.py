from domain.entities import Book
from repository.book_repository import BookRepository

# functiile testeaza repository-ul aplicatiei pentru carte
def test_getAll_repository_book():
    bookRepository = BookRepository()
    book1 = Book("15", "Title", "Description", "Author", 6)
    book2 = Book("16", "Title2", "Description2", "Author2", 8)
    bookRepository.addBook(book1)
    bookRepository.addBook(book2)

    books = bookRepository.getAll()
    assert len(books) == 2
    assert books[0].get_id() == "15"
    assert books[1].get_id() == "16"

def test_getById_repository_book():
    bookRepository = BookRepository()
    book1 = Book("15", "Title", "Description", "Author", 6)
    bookRepository.addBook(book1)

    book = bookRepository.getById("15")

    assert book.get_title() == "Title"

def test_addBook_repository_book():
    bookRepository = BookRepository()
    book = Book("15", "Title", "Description", "Author", 6)

    bookRepository.addBook(book)

    books = bookRepository.getAll()
    assert len(books) == 1
    assert books[0].get_id() == "15"

    try:
        bookRepository.addBook(book)
        assert False
    except KeyError:
        ...

def test_update_repository_book():
    bookRepository = BookRepository()
    book1 = Book("15", "Title1", "Description1", "Author1", 6)
    book2 = Book("15", "Title2", "Description2", "Author2", 7)
    book3 = Book("17", "Title3", "Description3", "Author3", 8)

    bookRepository.addBook(book1)
    bookRepository.update(book2)

    books = bookRepository.getAll()
    assert books[0].get_title() == "Title2"

    try:
        bookRepository.update(book3)
        assert False
    except KeyError:
        ...

def test_delete_repository_book():
    bookRepository = BookRepository()
    book = Book("15", "Title1", "Description1", "Author1", 6)
    bookRepository.addBook(book)

    bookRepository.delete(book.get_id())

    assert len(bookRepository.getAll()) == 0

    try:
        bookRepository.delete("23423")
        assert False
    except KeyError:
        ...