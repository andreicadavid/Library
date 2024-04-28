# clasele vor transmite erori pentru validarea datelor de intrare
class IdError(Exception):
    def __init__(self, id, message = "id cannot be negative!"):
        self.id = id
        self.message = message
        super().__init__(self.message)

class IdErrorEmpty(Exception):
    def __init__(self, id, message = "id cannot be empty!"):
        self.id = id
        self.message = message
        super().__init__(self.message)

class IdErrorNumeric(Exception):
    def __init__(self, id, message = "id must be numeric!"):
        self.id = id
        self.message = message
        super().__init__(self.message)

class TitleErrorEmpty(Exception):
    def __init__(self, title, message = "title cannot be empty!"):
        self.title = title
        self.message = message
        super().__init__(self.message)

class DescriptionErrorEmpty(Exception):
    def __init__(self, description, message = "description cannot be empty!"):
        self.description = description
        self.message = message
        super().__init__(self.message)

class AuthorErrorEmpty(Exception):
    def __init__(self, author, message = "author cannot be empty!"):
        self.author = author
        self.message = message
        super().__init__(self.message)

class AuthorErrorAlpha(Exception):
    def __init__(self, author, message = "author must contain only alphabetical letters!"):
        self.author = author
        self.message = message
        super().__init__(self.message)

class AuthorErrorUpper(Exception):
    def __init__(self, author, message = "the first letter of the author's name must be capitalized!"):
        self.author = author
        self.message = message
        super().__init__(self.message)

class CnpErrorEmpty(Exception):
    def __init__(self, cnp, message = "cnp cannot be empty!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorNegative(Exception):
    def __init__(self, cnp, message = "cnp cannot be negative!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorLength(Exception):
    def __init__(self, cnp, message = "cnp must contain 13 digits!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorS(Exception):
    def __init__(self, cnp, message = "component S must be between 1 and 8!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorNumeric(Exception):
    def __init__(self, cnp, message = "cnp must contain only positive digits!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorLL(Exception):
    def __init__(self, cnp, message = "component LL must be between 01 and 12!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorZZ(Exception):
    def __init__(self, cnp, message = "component ZZ must be between 01 and 31!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorJJ(Exception):
    def __init__(self, cnp, message = "component JJ must be between 01 and 52!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class CnpErrorInvalid(Exception):
    def __init__(self, cnp, message = "invalid cnp!"):
        self.cnp = cnp
        self.message = message
        super().__init__(self.message)

class RentErrorValue(Exception):
    def __init__(self, rent, message = "rent value cannot be negative!"):
        self.rent = rent
        self.message = message
        super().__init__(self.message)