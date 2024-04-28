from repository.book_repository import BookRepository
from repository.client_repository import ClientRepository
from domain.dto import *

class ReportsService:
    def __init__(self, clientRepository: ClientRepository, bookRepository: BookRepository):
        self.__clientRepository = clientRepository
        self.__bookrepository = bookRepository

    def sortNameRentalNr(self):
        clients_dto = self.__create_client_dto()
        clients_dto = sorted(clients_dto, key = lambda x: x.name)
        clients_dto = sorted(clients_dto, key = lambda x: x.list_nr)
        return clients_dto

    def twenty_percent(self):
        clients_dto = self.__create_client_dto()
        clients_dto = sorted(clients_dto, key = lambda x: x.list_nr, reverse = True)
        rez = (20 * len(clients_dto)) // 100
        rez += 1
        return clients_dto[:rez]

    def __create_client_dto(self):
        clients_dto = []
        for client in self.__clientRepository.getAll():
            dto = ClientDTOAssembler.create_client_dto(client)
            clients_dto.append(dto)
        return clients_dto