from domain.entities import Client
from repository.client_repository import ClientRepository
from repository.book_repository import BookRepository

class ClientService:
    def __init__(self, clientRepository: ClientRepository, bookRepository: BookRepository):
        # in ClientService se va crea un nou ClientRepository
        # in ClientService se va crea un nou BookRepository
        self.__clientRepository = clientRepository
        self.__bookrepository = bookRepository

    def getAll(self):
        # returneaza o lista cu toti clientii
        return self.__clientRepository.getAll()

    def addClient(self, idClient, name, cnp, listr):
        # adauga un nou client in dictionar daca acesta nu se afla deja in dictionar, in caz contar returneaza un KeyError
        client = Client(idClient, name, cnp, listr)
        self.__clientRepository.addClient(client)

    def update(self, idClient, nameNew, cnpNew, listrNew):
        # face update unui client daca se afla in dictionar, altfel returneaza un KeyError
        client = Client(idClient, nameNew, cnpNew, listrNew)
        self.__clientRepository.update(client)

    def delete(self, idClient):
        # sterge un client dupa un id daca se afla in dictionar, altfel returneaza un KeyError
        self.__clientRepository.delete(idClient)

    def findById(self, idClient):
        # in cazul in care exista un client dupa un id returneaza clientul altfel returneaza None
        return self.__clientRepository.getById(idClient)

    def rentBook(self, idBook, idClient):
        # verifica daca exista un client in dictionar dupa id-ul dat si adauga listei de carti inchiriate id-ul cartii transmise
        # in caz contrar modifica numarul de inchirieri la cartea cu id-ul transmis cu -1 si returneaza un KeyError
        if self.findById(idClient) is None:
            book = self.__bookrepository.getById(idBook)
            rentval = book.get_brn()
            rentval -= 1
            book.set_brn(rentval)
            self.__bookrepository.update(book)
            raise KeyError("there is no client with the given id!")
        client = self.__clientRepository.getById(idClient)
        listR = client.get_list_rent()
        listR.append(idBook)
        self.update(idClient, client.get_name(), client.get_cnp(), listR)

    def sortNameRentalNr(self):
        # sorteaza crescator lista de clienti cu carti inchiriate dupa nume iar mai apoi dupa numarul de carti inchiriate
        listCl = self.getAll()
        for i in listCl:
            if len(i.get_list_rent()) == 0:
                listCl.remove(i)

        aux = Client("0", "0", "0", [])

        for i in range(0, len(listCl) - 1):
            for j in range(i + 1, len(listCl)):
                name1 = listCl[i].get_name()
                name2 = listCl[j].get_name()
                if name1 > name2:
                    aux.set_id(listCl[i].get_id())
                    aux.set_name(listCl[i].get_name())
                    aux.set_cnp(listCl[i].get_cnp())
                    aux.set_list_rent(listCl[i].get_list_rent())

                    listCl[i].set_id(listCl[j].get_id())
                    listCl[i].set_name(listCl[j].get_name())
                    listCl[i].set_cnp(listCl[j].get_cnp())
                    listCl[i].set_list_rent(listCl[j].get_list_rent())

                    listCl[j].set_id(aux.get_id())
                    listCl[j].set_name(aux.get_name())
                    listCl[j].set_cnp(aux.get_cnp())
                    listCl[j].set_list_rent(aux.get_list_rent())

        for i in range(0, len(listCl) - 1):
            for j in range(i + 1, len(listCl)):
                l1 = listCl[i].get_list_rent()
                l1l = len(l1)
                l2 = listCl[j].get_list_rent()
                l2l = len(l2)
                if l1l > l2l:
                    aux.set_id(listCl[i].get_id())
                    aux.set_name(listCl[i].get_name())
                    aux.set_cnp(listCl[i].get_cnp())
                    aux.set_list_rent(listCl[i].get_list_rent())

                    listCl[i].set_id(listCl[j].get_id())
                    listCl[i].set_name(listCl[j].get_name())
                    listCl[i].set_cnp(listCl[j].get_cnp())
                    listCl[i].set_list_rent(listCl[j].get_list_rent())

                    listCl[j].set_id(aux.get_id())
                    listCl[j].set_name(aux.get_name())
                    listCl[j].set_cnp(aux.get_cnp())
                    listCl[j].set_list_rent(aux.get_list_rent())

        return listCl

    def twenty_percent(self):
        # sorteaza crescator lista de clienti cu carti inchiriate dupa numarul de carti inchiriate
        # si returneaza o lista cu primii 20% din lista
        l = self.getAll()
        for i in l:
            if len(i.get_list_rent()) == 0:
                l.remove(i)
        aux1 = Client("0", "0", "0", [])
        for i in range(0, len(l) - 1):
            for j in range(i + 1, len(l)):
                list1 = l[i].get_list_rent()
                list1_len = len(list1)
                list2 = l[j].get_list_rent()
                list2_len = len(list2)
                if(list1_len < list2_len):
                    aux1.set_id(l[i].get_id())
                    aux1.set_name(l[i].get_name())
                    aux1.set_cnp(l[i].get_cnp())
                    aux1.set_list_rent(l[i].get_list_rent())

                    l[i].set_id(l[j].get_id())
                    l[i].set_name(l[j].get_name())
                    l[i].set_cnp(l[j].get_cnp())
                    l[i].set_list_rent(l[j].get_list_rent())

                    l[j].set_id(aux1.get_id())
                    l[j].set_name(aux1.get_name())
                    l[j].set_cnp(aux1.get_cnp())
                    l[j].set_list_rent(aux1.get_list_rent())

        rez_list = []
        len_rez_list = (20 * len(l)) // 100
        len_rez_list += 1
        for i in range(0, len_rez_list):
            rez_list.append(l[i])
        return rez_list