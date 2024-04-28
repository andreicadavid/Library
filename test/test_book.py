from domain.entities import Book

# functiile testeaza domain-ul aplicatiei pentru carte
def testBook_get():
    book = Book("15", "Title", "Description", "Author", 6)

    assert book.get_id() == "15"
    assert book.get_title() == "Title"
    assert book.get_description() == "Description"
    assert book.get_author() == "Author"
    assert book.get_brn() == 6
    assert str(book) == "id: 15   title: Title   description: Description   author: Author   rent: 6"

def testBook_set():
    book = Book("15", "Title", "Description", "Author", 6)

    book.set_id("77")
    assert book.get_id() == "77"

    book.set_title("title new")
    assert book.get_title() == "title new"

    book.set_description("description new")
    assert book.get_description() == "description new"

    book.set_author("author new")
    assert book.get_author() == "author new"

    book.set_brn(66)
    assert book.get_brn() == 66