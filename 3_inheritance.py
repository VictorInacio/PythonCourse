# Create a super and derived classes

# https://docs.python.org/3/tutorial/classes.html

class Super:
    def __init__(self):
        pass


class Derived(Super):
    def __init__(self):
        # super().__init__()
        pass


d = Derived()

dir(d)
d.__doc__
d.__dict__
d.__class__
d.__init_subclass__
d.__subclasshook__
d.__weakref__
d.__hash__()


# Error classes
class FakeError:
    pass


raise FakeError


class GoodError(Exception):
    pass


# raise GoodError


# Polymorphism
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()
