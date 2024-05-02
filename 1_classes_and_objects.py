# 1_classes_and_objects.py

# https://docs.python.org/3/reference/compound_stmts.html#class-definitions

# Class declaration
class Person:
    firstname: str
    lastname: str

    # Init method
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # Instance method
    def printname(self):
        print(self.firstname, self.lastname)

    # Override method
    def __str__(self):
        return f"My name is: {self.firstname} {self.lastname}"


x1 = Person("John", "Doe")

x1.printname()
print(x1)

x1.firstname = "Victor"
x1.printname()
print(x1)

print(type(Person))
print(type(x1))

