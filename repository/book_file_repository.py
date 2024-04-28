from domain.entities import Book
from repository.book_repository import BookRepository
from test.input_data_validation import Validation_addBook
from test.errors import *

# clasa va adauga dintr-un fisier carti in BookRepository
class BookFileRepository(BookRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                book_list = line.split(",")
                if book_list[3][len(book_list[3]) - 1] == '\n':
                    book_list[3] = book_list[3][:-1]
                book = Book(book_list[0], book_list[1], book_list[2], book_list[3], 0)
                try:
                    validation_addBook = Validation_addBook(book_list[0], book_list[1], book_list[2], book_list[3])
                    validation_addBook.test_idBook()
                    validation_addBook.test_titleBook()
                    validation_addBook.test_descriptionBook()
                    validation_addBook.test_authorBook()
                    super().addBook(book)
                except KeyError as e:
                    print(e)
                except IdError as ie:
                    print(ie)
                except IdErrorEmpty as iee:
                    print(iee)
                except IdErrorNumeric as ien:
                    print(ien)
                except TitleErrorEmpty as tee:
                    print(tee)
                except DescriptionErrorEmpty as dee:
                    print(dee)
                except AuthorErrorEmpty as aee:
                    print(aee)
                except AuthorErrorAlpha as aea:
                    print(aea)
                except AuthorErrorUpper as aeu:
                    print(aeu)
        f.close()

    def addBook(self, book):
        #with open(self.__file_name, "a") as f:
            #f.write("\n" + book.get_id() + "," + book.get_title() + "," + book.get_description() + "," + book.get_author() + "," + str(book.get_brn()))
        super().addBook(book)
        self.write_in_file()

    def update(self, bookNew):
        super().update(bookNew)
        self.write_in_file()

    def delete(self, idBook):
        super().delete(idBook)
        self.write_in_file()

    def write_in_file(self):
        try:
            f = open(self.__file_name, "w")
            books_list = super().getAll()
            for book in books_list:
                id = book.get_id()
                title = book.get_title()
                description = book.get_description()
                author = book.get_author()
                brn = book.get_brn()
                line = id + "," + title + "," + description + "," + author + "," + str(brn) + "\n"
                f.write(line)
            f.close()
        except IOError as IOE:
            print(IOE)