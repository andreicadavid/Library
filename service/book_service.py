from domain.entities import Book
from repository.book_repository import BookRepository

class BookService:
    def __init__(self, bookRepository: BookRepository):
        # in BookService se va crea un nou BookRepository
        self.__bookRepository = bookRepository

    def getAll(self):
        # returneaza o lista cu toate cartile
        return self.__bookRepository.getAll()

    def addBook(self, id, title, description, author, brn):
        # adauga o noua carte in dictionar daca aceasta nu se afla deja in dictionar, in caz contar returneaza un KeyError
        book = Book(id, title, description, author, brn)
        self.__bookRepository.addBook(book)

    def update(self, id, titleNew, descriptionNew, authorNew, brnNew):
        # face update unei carti daca se afla in dictionar, altfel returneaza un KeyError
        book = Book(id, titleNew, descriptionNew, authorNew, brnNew)
        self.__bookRepository.update(book)

    def delete(self, id):
        # sterge o carte dupa un id daca se afla in dictionar, altfel returneaza un KeyError
        self.__bookRepository.delete(id)

    def findById(self, id):
        # in cazul in care exista o carte dupa un id o returneaza cartea altfel returneaza None
        return self.__bookRepository.getById(id)

    def rentBookById(self, idBook):
        # verifica daca exista o carte in dictionar dupa id-ul dat si incrementeaza cu 1 numarul de carti inchiriate
        # in caz contrar returneaza un KeyError
        if self.findById(idBook) is None:
            raise KeyError("there is no book with the given id!")
        book = self.__bookRepository.getById(idBook)
        book_rent_nr = book.get_brn()
        book_rent_nr += 1
        self.update(idBook, book.get_title(), book.get_description(), book.get_author(), book_rent_nr)

    def rentBookSort(self):
        # returneaza o lista de carti sortata descrescator dupa numarul de carti inchiriate
        listBooks = self.__bookRepository.getAll()
        aux = Book("0", "0", "0", "0")
        for i in range(0, len(listBooks) - 1):
            for j in range(i + 1, len(listBooks)):
                if listBooks[i].get_brn() < listBooks[j].get_brn():
                    aux.set_id(listBooks[i].get_id())
                    aux.set_title(listBooks[i].get_title())
                    aux.set_description(listBooks[i].get_description())
                    aux.set_author(listBooks[i].get_author())
                    aux.set_brn(listBooks[i].get_brn())

                    listBooks[i].set_id(listBooks[j].get_id())
                    listBooks[i].set_title(listBooks[j].get_title())
                    listBooks[i].set_description(listBooks[j].get_description())
                    listBooks[i].set_author(listBooks[j].get_author())
                    listBooks[i].set_brn(listBooks[j].get_brn())

                    listBooks[j].set_id(aux.get_id())
                    listBooks[j].set_title(aux.get_title())
                    listBooks[j].set_description(aux.get_description())
                    listBooks[j].set_author(aux.get_author())
                    listBooks[j].set_brn(aux.get_brn())
        return listBooks