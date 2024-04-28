from test.errors import *

# in clasele ce urmeaza se vor valida datele de intrare
class Validation_addBook():
    def __init__(self, idBook, titleBook, descriptionBook, authorBook):
        self.idBook = idBook
        self.titleBook = titleBook
        self.descriptionBook = descriptionBook
        self.authorBook = authorBook

    def test_idBook(self):
        if len(self.idBook) == 0:
            raise IdErrorEmpty(self.idBook)
        if self.idBook[0] == "-":
            raise IdError(self.idBook)
        if self.idBook.isnumeric() == False:
            raise IdErrorNumeric(self.idBook)

    def test_titleBook(self):
        if len(self.titleBook) == 0:
            raise TitleErrorEmpty(self.titleBook)

    def test_descriptionBook(self):
        if len(self.descriptionBook) == 0:
            raise DescriptionErrorEmpty(self.descriptionBook)

    def test_authorBook(self):
        if len(self.authorBook) == 0:
            raise AuthorErrorEmpty(self.authorBook)

        author_name = self.authorBook.split()
        for name in author_name:
            if name.isalpha() == False:
                raise AuthorErrorAlpha(name)

        if self.authorBook[0].isupper() == False:
            raise AuthorErrorUpper(self.authorBook)

class Validation_addClient():
    def __init__(self, idClient, nameClient, cnpClient):
        self.idClient = idClient
        self.nameClient = nameClient
        self.cnpClient = cnpClient

    def test_idClient(self):
        if len(self.idClient) == 0:
            raise IdErrorEmpty(self.idClient)
        if self.idClient[0] == "-":
            raise IdError(self.idClient)
        if self.idClient.isnumeric() == False:
            raise IdErrorNumeric(self.idClient)

    def test_nameClient(self):
        if len(self.nameClient) == 0:
            raise AuthorErrorEmpty(self.nameClient)

        client_name = self.nameClient.split()
        for name in client_name:
            if name.isalpha() == False:
                raise AuthorErrorAlpha(name)

        if self.nameClient[0].isupper() == False:
            raise AuthorErrorUpper(self.nameClient)

    def test_cnpClient(self):
        if len(self.cnpClient) == 0:
            raise CnpErrorEmpty(self.cnpClient)
        if self.cnpClient[0] == "-":
            raise CnpErrorNegative(self.cnpClient)
        if self.cnpClient.isnumeric() == False:
            raise CnpErrorNumeric(self.cnpClient)
        if not len(self.cnpClient) == 13:
            raise CnpErrorLength(self.cnpClient)

        #------S------#
        if not (int(self.cnpClient[0]) >= 1 and int(self.cnpClient[0]) <= 8):
            raise CnpErrorS(self.cnpClient)
        # ------S------#

        # ------LL------#
        LL = self.cnpClient[3:5]
        LL_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        if LL not in LL_list:
            raise CnpErrorLL(self.cnpClient)
        # ------LL------#

        # ------ZZ------#
        ZZ = self.cnpClient[5:7]
        ZZ_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        if ZZ not in ZZ_list:
            raise CnpErrorZZ(self.cnpClient)
        # ------ZZ------#

        # ------JJ------#
        JJ = self.cnpClient[7:9]
        JJ_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
        if JJ not in JJ_list:
            if not(int(JJ) >= 10 and int(JJ) <= 52):
                raise CnpErrorJJ(self.cnpClient)
        # ------JJ------#

        if self.cnpClient[11] == "0":
            raise CnpErrorInvalid(self.cnpClient)

class Validation_updateBook():
    def __init__(self, idBook, titleBook, descriptionBook, authorBook, rentBook):
        self.idBook = idBook
        self.titleBook = titleBook
        self.descriptionBook = descriptionBook
        self.authorBook = authorBook
        self.rentBook = rentBook

    def test_idBook(self):
        if len(self.idBook) == 0:
            raise IdErrorEmpty(self.idBook)
        if self.idBook[0] == "-":
            raise IdError(self.idBook)
        if self.idBook.isnumeric() == False:
            raise IdErrorNumeric(self.idBook)

    def test_titleBook(self):
        if len(self.titleBook) == 0:
            raise TitleErrorEmpty(self.titleBook)

    def test_descriptionBook(self):
        if len(self.descriptionBook) == 0:
            raise DescriptionErrorEmpty(self.descriptionBook)

    def test_authorBook(self):
        if len(self.authorBook) == 0:
            raise AuthorErrorEmpty(self.authorBook)

        author_name = self.authorBook.split()
        for name in author_name:
            if name.isalpha() == False:
                raise AuthorErrorAlpha(name)

        if self.authorBook[0].isupper() == False:
            raise AuthorErrorUpper(self.authorBook)

    def test_rentBook(self):
        if int(self.rentBook) < 0:
            raise RentErrorValue(self.rentBook)

class Validation_updateClient():
    def __init__(self, idClient, nameClient, cnpClient):
        self.idClient = idClient
        self.nameClient = nameClient
        self.cnpClient = cnpClient

    def test_idClient(self):
        if len(self.idClient) == 0:
            raise IdErrorEmpty(self.idClient)
        if self.idClient[0] == "-":
            raise IdError(self.idClient)
        if self.idClient.isnumeric() == False:
            raise IdErrorNumeric(self.idClient)

    def test_nameClient(self):
        if len(self.nameClient) == 0:
            raise AuthorErrorEmpty(self.nameClient)

        client_name = self.nameClient.split()
        for name in client_name:
            if name.isalpha() == False:
                raise AuthorErrorAlpha(name)

        if self.nameClient[0].isupper() == False:
            raise AuthorErrorUpper(self.nameClient)

    def test_cnpClient(self):
        if len(self.cnpClient) == 0:
            raise CnpErrorEmpty(self.cnpClient)
        if self.cnpClient[0] == "-":
            raise CnpErrorNegative(self.cnpClient)
        if self.cnpClient.isnumeric() == False:
            raise CnpErrorNumeric(self.cnpClient)
        if not len(self.cnpClient) == 13:
            raise CnpErrorLength(self.cnpClient)

        #------S------#
        if not (int(self.cnpClient[0]) >= 1 and int(self.cnpClient[0]) <= 8):
            raise CnpErrorS(self.cnpClient)
        # ------S------#

        # ------LL------#
        LL = self.cnpClient[3:5]
        LL_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        if LL not in LL_list:
            raise CnpErrorLL(self.cnpClient)
        # ------LL------#

        # ------ZZ------#
        ZZ = self.cnpClient[5:7]
        ZZ_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        if ZZ not in ZZ_list:
            raise CnpErrorZZ(self.cnpClient)
        # ------ZZ------#

        # ------JJ------#
        JJ = self.cnpClient[7:9]
        JJ_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
        if JJ not in JJ_list:
            if not(int(JJ) >= 10 and int(JJ) <= 52):
                raise CnpErrorJJ(self.cnpClient)
        # ------JJ------#

        if self.cnpClient[11] == "0":
            raise CnpErrorInvalid(self.cnpClient)