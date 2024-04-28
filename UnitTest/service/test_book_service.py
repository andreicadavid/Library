import unittest
from repository.book_repository import BookRepository
from service.book_service import BookService

class TestBookService(unittest.TestCase):
    def setUp(self):
        self.bookRepository = BookRepository()
        self.bookService = BookService(self.bookRepository)
        self.bookService.addBook("15", "Title", "Description", "Author", 6)
        self.bookService.addBook("16", "Title2", "Description", "Author", 5)

    def test_getAll(self):
        books = self.bookService.getAll()
        self.assertEqual(books[0].get_id(), "15")
        self.assertEqual(books[1].get_id(), "16")

    def test_addBook(self):
        self.bookService.addBook("77", "Title", "Description", "Author", 623)
        books = self.bookService.getAll()
        self.assertEqual(books[2].get_id(), "77")

        try:
            self.bookService.addBook("77", "Title", "Description", "Author", 623)
            assert False
        except KeyError:
            assert True

    def test_update(self):
        self.bookService.update("15", "TitleNew", "Description", "Author", 6)
        books = self.bookService.getAll()
        self.assertEqual(books[0].get_title(), "TitleNew")

        try:
            self.bookService.update("444", "TitleNew", "Description", "Author", 6)
            assert False
        except KeyError:
            assert True

    def test_delete(self):
        self.bookService.delete("16")
        books = self.bookService.getAll()
        self.assertEqual(len(books), 1)

        try:
            self.bookService.delete("23423432")
            assert False
        except KeyError:
            assert True

    def test_findById(self):
        book = self.bookService.findById("16")
        self.assertEqual(book.get_title(), "Title2")
        self.assertEqual(book.get_id(), "16")

        book2 = self.bookService.findById("423423")
        self.assertIsNone(book2)

    def test_rentBookById(self):
        self.bookService.rentBookById("15")
        books = self.bookService.getAll()
        self.assertEqual(books[0].get_brn(), 7)

        try:
            self.bookService.rentBookById("23423")
            assert False
        except KeyError:
            assert True

    def test_rentBookSort(self):
        self.bookService.addBook("17", "Title3", "description", "AuthorNew", 9)
        self.bookService.rentBookSort()
        books = self.bookService.getAll()

        self.assertEqual(len(books), 3)
        self.assertEqual(books[0].get_id(), "17")
        self.assertEqual(books[1].get_id(), "15")
        self.assertEqual(books[2].get_id(), "16")

        self.assertEqual(books[0].get_title(), "Title3")
        self.assertEqual(books[1].get_title(), "Title")
        self.assertEqual(books[2].get_title(), "Title2")

        self.assertEqual(books[0].get_author(), "AuthorNew")
        self.assertEqual(books[1].get_author(), "Author")
        self.assertEqual(books[2].get_author(), "Author")

        self.assertEqual(books[0].get_description(), "description")
        self.assertEqual(books[1].get_description(), "Description")
        self.assertEqual(books[2].get_description(), "Description")

        self.assertEqual(books[0].get_brn(), 9)
        self.assertEqual(books[1].get_brn(), 6)
        self.assertEqual(books[2].get_brn(), 5)

if __name__ == '__main__':
    unittest.main()