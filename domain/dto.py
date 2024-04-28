from dataclasses import dataclass

@dataclass
class ClientDTO:
    name: str
    list_nr: int
    rental_list: list

class ClientDTOAssembler:
    @staticmethod
    def create_client_dto(client):
        name = client.get_name()
        list_nr = len(client.get_list_rent())
        rental_list = client.get_list_rent()
        return ClientDTO(name, list_nr, rental_list)