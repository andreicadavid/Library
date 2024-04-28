import unittest
from domain.entities import Book
from repository.book_repository import BookRepository

class TestBookRepository(unittest.TestCase):
    def setUp(self):
        self.bookRepository = BookRepository()
        self.book1 = Book("15", "Title", "Description", "Author", 6)
        self.book2 = Book("16", "Title2", "Description2", "Author", 8)
        self.bookRepository.addBook(self.book1)
        self.bookRepository.addBook(self.book2)

    def test_getAll(self):
        books = self.bookRepository.getAll()
        self.assertTrue(len(books) == 2, "Incorrect length")
        self.assertTrue(books[0].get_id() == "15", "First book id should be 15")
        self.assertTrue(books[1].get_id() == "16", "Second book id should be 16")

    def test_getById(self):
        book1 = self.bookRepository.getById("15")
        self.assertEqual(book1.get_title(), "Title")

        book2 = self.bookRepository.getById("16")
        self.assertEqual(book2.get_brn(), 8)

    def test_addBook(self):
        book = Book("18", "Title3", "Description3", "Author", 831)
        self.bookRepository.addBook(book)
        books = self.bookRepository.getAll()
        self.assertEqual(books[2].get_id(), "18")

        try:
            self.bookRepository.addBook(self.book1)
            assert False
        except KeyError:
            assert True

    def test_update(self):
        book = Book("15", "Title2", "Description2", "Author2", 7)
        self.bookRepository.update(book)
        books = self.bookRepository.getAll()
        self.assertEqual(books[0].get_title(), "Title2")

        try:
            book_new = Book("17", "Title2", "Description2", "Author2", 7)
            self.bookRepository.update(book_new)
            assert False
        except KeyError:
            assert True

    def test_delete(self):
        self.bookRepository.delete(self.book1.get_id())
        books = self.bookRepository.getAll()
        self.assertEqual(books[0].get_id(), "16")

        try:
            self.bookRepository.delete("534534")
            assert False
        except KeyError:
            assert True

if __name__ == '__main__':
    unittest.main()