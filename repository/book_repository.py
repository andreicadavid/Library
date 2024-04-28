class BookRepository:
    def __init__(self):
        # se va crea un dictionar pentru a stoca datele cartii
        self.__all_books_dict = {}

    def getAll(self):
        # returneaza o lista cu toate cartile
        return list(self.__all_books_dict.values())

    def getById(self, idBook):
        # in cazul in care exista o carte dupa un id o returneaza cartea altfel returneaza None
        if idBook in self.__all_books_dict:
            return self.__all_books_dict[idBook]
        return None

    def addBook(self, book):
        # adauga o noua carte in dictionar daca aceasta nu se afla deja in dictionar, in caz contar returneaza un KeyError
        if self.getById(book.get_id()) is not None:
            raise KeyError("there is already a book with the given id!")
        self.__all_books_dict[book.get_id()] = book

    def update(self, bookNew):
        # face update unei carti daca se afla in dictionar, altfel returneaza un KeyError
        if self.getById(bookNew.get_id()) is None:
            raise KeyError("there is no book with the given id!")
        self.__all_books_dict[bookNew.get_id()] = bookNew

    def delete(self, idBook):
        # sterge o carte dupa un id daca se afla in dictionar, altfel returneaza un KeyError
        if self.getById(idBook) is None:
            raise KeyError("there is no book with the given id!")
        self.__all_books_dict.pop(idBook)