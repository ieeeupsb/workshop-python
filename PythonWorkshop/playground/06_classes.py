class aClass:
    # static parameters (all instances have these)
    a = 1234
    b = "lol"
    z = [1, 2, 3]
    # this class has no constructor

    def hello(self):  # method of class
        print("Hello, world")


c = aClass()
d = aClass()

c.hello()

print(c.a)  # prints 1234
d.a = 9999
print(d.a)  # prints 9999


# Class inheritance
from random import randrange


class Animal:
    real = True

    # class constructor
    def __init__(self, tax, age, avgLifespan, name):
        self.alive = True
        self.name = name
        self.taxonomy = tax
        self.age = age
        self.lifespan = avgLifespan

    def getOlder(self):
        self.age += 1
        if(self.alive and randrange(self.lifespan - 5, self.lifespan + 5) < self.age):
            self.alive = False
            real = False
            print(self.name + " has died")

    def convertAge(self):
        return self.age


class Human(Animal):  # Human inherits from Animal
    def __init__(self, age, name):  # new constructor
        # calls parent class's constructor
        super(Human, self).__init__("Homo Sapiens Sapiens", age, 85, name)

    def getAge(self):  # implements a new method, not present in Human
        if not self.alive:
            return "dead"
        return self.age


class Dog(Animal):
    def __init__(self, age, name):
        super(Dog, self).__init__("Canis lupus familiaris", age, 10, name)

    def getAge(self):
        if not self.alive:
            return "dead"
        return self.convertAge()

    def convertAge(self):  # overrides a method from its parent
        if self.age <= 2:
            return self.age * 10.5
        else:
            return 21 + (self.age - 2) * 4


alex = Human(0, "Alex")
fido = Dog(0, "Fido")
while alex.alive or fido.alive:
    alex.getOlder()
    fido.getOlder()
    print("%s age is: %s and %s age is %s" %
          (alex.name, alex.getAge(), fido.name, fido.getAge()))
print("Both are dead, %s lived %d human years and %s lived %d dog years" %
      (alex.name, alex.convertAge(), fido.name, fido.convertAge()))
