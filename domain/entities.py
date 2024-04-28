class Book:
    def __init__(self, id, title, description, author, brn = 0):
        # se vor atribui valori atributelor din clasa Book
        self.__id = id
        self.__title = title
        self.__description = description
        self.__author = author
        self.__brn = brn

    def get_id(self):
        # returneaza id-ul cartii
        return self.__id

    def get_title(self):
        # returneaza titlul cartii
        return self.__title

    def get_description(self):
        # returneaza descrierea cartii
        return self.__description

    def get_author(self):
        # returneaza autorul cartii
        return self.__author

    def get_brn(self):
        # returneaza numarul de carti inchiriate
        return self.__brn

    def set_id(self, id_new):
        # atribuie un nou id
        self.__id = id_new

    def set_title(self, title_new):
        # atribuie un nou titlu
        self.__title = title_new

    def set_description(self, description_new):
        # atribuie o noua descriere
        self.__description = description_new

    def set_author(self, author_new):
        # atribuie un nou autor
        self.__author = author_new

    def set_brn(self, brn_new):
        # atribuie o noua valoare pentru numarul de carti inchiriate
        self.__brn = brn_new

    def __str__(self):
        # returneaza un sir de caractere care contine toate atributele cartii impreuna cu valorile lor
        return f"id: {self.__id}   title: {self.__title}   description: {self.__description}   author: {self.__author}   rent: {self.__brn}"

class Client:
    def __init__(self, idClient, name, cnp, list_rent = []):
        # se vor atribui valori atributelor din clasa Client
        self.__idClient = idClient
        self.__name = name
        self.__cnp = cnp
        self.__list_rent = list_rent

    def get_id(self):
        # returneaza id-ul clientului
        return self.__idClient

    def get_name(self):
        # returneaza numele clientului
        return self.__name

    def get_cnp(self):
        # returneaza cnp-ul clientului
        return self.__cnp

    def get_list_rent(self):
        # returneaza lista de carti inchiriate
        return self.__list_rent

    def set_id(self, id_new):
        # atribuie un nou id clientului
        self.__idClient = id_new

    def set_name(self, name_new):
        # atribuie un nou nume clientului
        self.__name = name_new

    def set_cnp(self, cnp_new):
        # atribuie un nou cnp clientului
        self.__cnp = cnp_new

    def set_list_rent(self, list_rent_new):
        # atribuie o noua lista de carti inchiriate clientului
        self.__list_rent = list_rent_new

    def __str__(self):
        # returneaza un sir de caractere care contine toate atributele clientului impreuna cu valorile lor
        return f"id: {self.__idClient}   name: {self.__name}   cnp: {self.__cnp}   RentedBooks: {self.__list_rent}"