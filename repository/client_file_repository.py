from domain.entities import Client
from repository.client_repository import ClientRepository
from test.input_data_validation import Validation_addClient
from test.errors import *

# clasa va adauga dintr-un fisier clienti in ClientRepository
class ClientFileRepository(ClientRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                client_list = line.split(",")
                if client_list[2][len(client_list[2]) - 1] == '\n':
                    client_list[2] = client_list[2][:-1]
                client = Client(client_list[0], client_list[1], client_list[2], [])
                try:
                    validation_addClient = Validation_addClient(client_list[0], client_list[1], client_list[2])
                    validation_addClient.test_idClient()
                    validation_addClient.test_nameClient()
                    validation_addClient.test_cnpClient()
                    super().addClient(client)
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
        f.close()

    def addClient(self, client):
        #with open(self.__file_name, "a") as f:
            #f.write("\n" + client.get_id() + "," + client.get_name() + "," + client.get_cnp() + "," + str(client.get_list_rent()))
        super().addClient(client)
        self.write_in_file()

    def update(self, clientNew):
        super().update(clientNew)
        self.write_in_file()

    def delete(self, idClient):
        super().delete(idClient)
        self.write_in_file()

    def write_in_file(self):
        try:
            f = open(self.__file_name, "w")
            clients_list = super().getAll()
            for client in clients_list:
                id = client.get_id()
                name = client.get_name()
                cnp = client.get_cnp()
                list_rent = client.get_list_rent()
                line = id + "," + name + "," + cnp + "," + str(list_rent) + "\n"
                f.write(line)
            f.close()
        except IOError as IOE:
            print(IOE)