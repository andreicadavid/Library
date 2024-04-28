from domain.entities import Client

# functiile testeaza domain-ul aplicatiei pentru client
def testClient_get():
    client = Client("13", "name", "5030326260056", [1, 2])

    assert client.get_id() == "13"
    assert client.get_name() == "name"
    assert client.get_cnp() == "5030326260056"
    assert client.get_list_rent() == [1, 2]
    assert str(client) == "id: 13   name: name   cnp: 5030326260056   RentedBooks: [1, 2]"

def testClient_set():
    client = Client("13", "name", "5030326260056", [1, 2])

    client.set_id("44")
    assert client.get_id() == "44"

    client.set_name("n")
    assert client.get_name() == "n"

    client.set_cnp("5030326260055")
    assert client.get_cnp() == "5030326260055"

    client.set_list_rent([1, 2, 3, 4])
    assert client.get_list_rent() == [1, 2, 3, 4]