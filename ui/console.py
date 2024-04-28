from service.book_service import BookService
from service.client_service import ClientService
from service.client_service_reports import ReportsService
from test.input_data_validation import *

class Console:
    def __init__(self, bookService: BookService, clientService: ClientService, reportsService: ReportsService):
        # in Console se va crea un nou BookService
        # in Console se va crea un nou ClientService
        self.__bookService = bookService
        self.__clientService = clientService
        self.__reportsService = reportsService

    def addBook(self):
        try:
            # in functie se vor citi de la tastatura datele cartii
            idBook = input("Enter the id of the book: ")
            titleBook = input("Enter the title of the book: ")
            descriptionBook = input("Enter the description of the book: ")
            authorBook = input("Enter the author of the book: ")
            rentBook = 0
            validation_addBook = Validation_addBook(idBook, titleBook, descriptionBook, authorBook)
            validation_addBook.test_idBook()
            validation_addBook.test_titleBook()
            validation_addBook.test_descriptionBook()
            validation_addBook.test_authorBook()
            self.__bookService.addBook(idBook, titleBook, descriptionBook, authorBook, rentBook)
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

    def addClient(self):
        try:
            # in functie se vor citi de la tastatura datele clientului
            idClient = input("Enter the id of the client: ")
            nameClient = input("Enter the name of the client: ")
            cnpClient = input("Enter the cnp of the client: ")
            listrClient = []
            validation_addClient = Validation_addClient(idClient, nameClient, cnpClient)
            validation_addClient.test_idClient()
            validation_addClient.test_nameClient()
            validation_addClient.test_cnpClient()
            self.__clientService.addClient(idClient, nameClient, cnpClient, listrClient)
        except KeyError as e:
            print(e)
        except IdErrorEmpty as iee:
            print(iee)
        except IdError as ie:
            print(ie)
        except IdErrorNumeric as ien:
            print(ien)
        except AuthorErrorEmpty as aee:
            print(aee)
        except AuthorErrorAlpha as aea:
            print(aea)
        except AuthorErrorUpper as aeu:
            print(aeu)
        except CnpErrorEmpty as cee:
            print(cee)
        except CnpErrorNegative as cen:
            print(cen)
        except CnpErrorLength as cel:
            print(cel)
        except CnpErrorS as ces:
            print(ces)
        except CnpErrorNumeric as cenu:
            print(cenu)
        except CnpErrorLL as cell:
            print(cell)
        except CnpErrorZZ as cezz:
            print(cezz)
        except CnpErrorJJ as cejj:
            print(cejj)
        except CnpErrorInvalid as cei:
            print(cei)

    def updateBook(self):
        try:
            # in functie se vor citi date noi de la tastatura pentru o carte identificata printr-un id
            idBook = input("Enter the id of the book you want to modify: ")
            titleBookNew = input("Enter the new title of the book: ")
            descriptionBookNew = input("Enter the new description of the book: ")
            authorBookNew = input("Enter the new author of the book: ")
            rentBookNew = input("Enter the new rental number of the book: ")
            validation_updateBook = Validation_updateBook(idBook, titleBookNew, descriptionBookNew, authorBookNew,
                                                          rentBookNew)
            validation_updateBook.test_idBook()
            validation_updateBook.test_titleBook()
            validation_updateBook.test_descriptionBook()
            validation_updateBook.test_authorBook()
            validation_updateBook.test_rentBook()
            self.__bookService.update(idBook, titleBookNew, descriptionBookNew, authorBookNew, rentBookNew)
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
        except RentErrorValue as rev:
            print(rev)

    def updateClient(self):
        try:
            # in functie se vor citi date noi de la tastatura pentru un client identificat printr-un id
            idClient = input("Enter the id of the client you want to modify: ")
            nameClientNew = input("Enter the new name of the client: ")
            cnpClientNew = input("Enter the new cnp of the client: ")
            listrNew = []
            list_len = int(input("Enter the length of the rental list: "))
            i = 0
            while i < list_len:
                b_id = input("Enter the id of the book you want to put in rental list: ")
                listrNew.append(b_id)
                i += 1
            validation_updateClient = Validation_updateClient(idClient, nameClientNew, cnpClientNew)
            validation_updateClient.test_idClient()
            validation_updateClient.test_nameClient()
            validation_updateClient.test_cnpClient()
            self.__clientService.update(idClient, nameClientNew, cnpClientNew, listrNew)
        except KeyError as e:
            print(e)
        except IdErrorEmpty as iee:
            print(iee)
        except IdError as ie:
            print(ie)
        except IdErrorNumeric as ien:
            print(ien)
        except AuthorErrorEmpty as aee:
            print(aee)
        except AuthorErrorAlpha as aea:
            print(aea)
        except AuthorErrorUpper as aeu:
            print(aeu)
        except CnpErrorEmpty as cee:
            print(cee)
        except CnpErrorNegative as cen:
            print(cen)
        except CnpErrorLength as cel:
            print(cel)
        except CnpErrorS as ces:
            print(ces)
        except CnpErrorNumeric as cenu:
            print(cenu)
        except CnpErrorLL as cell:
            print(cell)
        except CnpErrorZZ as cezz:
            print(cezz)
        except CnpErrorJJ as cejj:
            print(cejj)
        except CnpErrorInvalid as cei:
            print(cei)

    def deleteBook(self):
        try:
            # in functie se citeste id-ul cartii care ulterior va fi stearsa
            idBook = input("Enter the id of the book you want to delete: ")
            self.__bookService.delete(idBook)
        except KeyError as e:
            print(e)

    def deleteClient(self):
        try:
            # in functie se citeste id-ul clientului care ulterior va fi sters
            idClient = input("Enter the id of the client you want to delete: ")
            self.__clientService.delete(idClient)
        except KeyError as e:
            print(e)

    def findByIdBook(self):
        try:
            # in functie se citeste id-ul cartii prin care aceasta va fi cautata
            idBook = input("Enter the id of the book you want to find: ")
            b = self.__bookService.findById(idBook)
            if b is None:
                raise KeyError("there is no book with the given id!")
            print(b)
        except KeyError as e:
            print(e)

    def findByIdClient(self):
        try:
            # in functie se citeste id-ul clientului prin care acesta va fi cautat
            idClient = input("Enter the id of the client you want to find: ")
            c = self.__clientService.findById(idClient)
            if c is None:
                raise KeyError("here is no client with the given id!")
            print(c)
        except KeyError as e:
            print(e)

    def rentBook(self):
        try:
            # in functie se citeste id-ul cartii pe care utilizatorul doreste sa o inchirieze
            # iar mai apoi id-ul clientului caruia sa i se atribuie cartea inchiriata
            self.printAllBooks(self.__bookService.getAll())
            idBookRent = input("Enter the id of the book you want to rent: ")
            self.__bookService.rentBookById(idBookRent)
            self.printAllClients(self.__clientService.getAll())
            idClientRent = input("Enter the id of the client who will rent the book: ")
            self.__clientService.rentBook(idBookRent, idClientRent)
        except KeyError as e:
            print(e)

    def rentBookSort(self):
        try:
            # functia primeste o lista sortata descrescator dupa numarul de inchirieri
            # si apoi transmite lista primita catre o functie care o va afisa
            self.printAllBooks(self.__bookService.rentBookSort())
        except KeyError as e:
            print(e)

    def sortNameRentalNumber(self):
        try:
            # functia primeste o lista sortata crescator dupa nume si numarul de inchirieri
            # si apoi transmite lista primita catre o functie care o va afisa
            self.print_sortNameRentalNumber(self.__clientService.sortNameRentalNr())
            print("---------------------------------------------------")
            self.print_sortNameRentalNumber_second(self.__reportsService.sortNameRentalNr())
        except KeyError as e:
            print(e)

    def first_twenty_percent(self):
        try:
            # functia primeste o lista cu primii 20% clienti sortata crescator dupa numarul de inchirieri
            # si apoi transmite lista primita catre o functie care o va afisa
            self.print_sortNameRentalNumber(self.__clientService.twenty_percent())
            print("---------------------------------------------------")
            self.print_sortNameRentalNumber_second(self.__reportsService.twenty_percent())
        except KeyError as e:
            print(e)

    def print_sortNameRentalNumber(self, sortedList):
        # functia afiseaza o lista primita
        for o in sortedList:
            print(f"name: {o.get_name()}   RentedBooks: {o.get_list_rent()}")

    def print_sortNameRentalNumber_second(self, sortedList):
        # functia afiseaza o lista primita
        for o in sortedList:
            print(f"name: {o.name}   RentedBooks: {o.rental_list}")

    def printAllBooks(self, listOfBooks):
        # functia afiseaza o lista primita
        for i in listOfBooks:
            print(i)

    def printAllClients(self, listOfClients):
        # functia afiseaza o lista primita
        for j in listOfClients:
            print(j)

    def printMenu(self):
        # meniul aplicatiei
        print("1.  Add book")
        print("2.  Update book")
        print("3.  Delete book")
        print("4.  Find a book by id")
        print("5.  Add client")
        print("6.  Update client")
        print("7.  Delete client")
        print("8.  Find a client by id")
        print("9.  Rent a book")
        print("10. The most rented books")
        print("11. Clients with rented books ordered by name, by the number of rented books")
        print("12. First 20% of the most active customers")
        print("b.  Print all books")
        print("c.  Print all clients")
        print("e.  Exit")

    def Menu(self):
        # functia permite introducerea de la tastatura a unei optiuni din meniul dat
        while True:
            self.printMenu()
            op = input("Choose the option: ")
            if op == "1":
                self.addBook()
            elif op == "2":
                self.updateBook()
            elif op == "3":
                self.deleteBook()
            elif op == "4":
                self.findByIdBook()
            elif op == "5":
                self.addClient()
            elif op == "6":
                self.updateClient()
            elif op == "7":
                self.deleteClient()
            elif op == "8":
                self.findByIdClient()
            elif op == "9":
                self.rentBook()
            elif op == "10":
                self.rentBookSort()
            elif op == "11":
                self.sortNameRentalNumber()
            elif op == "12":
                self.first_twenty_percent()
            elif op == "b":
                self.printAllBooks(self.__bookService.getAll())
            elif op == "c":
                self.printAllClients(self.__clientService.getAll())
            elif op == "e":
                break
            else:
                print("invalid option, select another one!")