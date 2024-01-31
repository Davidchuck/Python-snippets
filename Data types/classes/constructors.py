class Animals:
    def __init__(self, name, species): #constructor
        self.name = name
        self.species = species
    def DomesticAnimals(self):
        print("This animal is a domesticated animal.")

Dog =Animals('Scobby','RotWailer')
print('My dogs Name is: ',Dog.name)

class Person:
    def __init__(self, name):
        self.name=name
    def talk(self):
        print("My name is ", self.name)

person1=Person('James')
person1.talk()