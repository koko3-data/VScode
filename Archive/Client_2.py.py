class Person:
    def __init__ (self, name :str, phone_number: str):
        self.name =name
        self.phone_number = phone_number

    def describe(self):
        return {self.name, self.phone_number}


class Client(Person):
    super()

bob = Client("Bob","+48-881278182")
bob.describe()