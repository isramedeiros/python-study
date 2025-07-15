class Person: # defines a class – blueprint for objects that represent people
    def __init__(self, name): # initializing the object
        self.name = name

person1 = Person("Francesco Virgulini") # instantiating person 1
person2 = Person("Chick Hicks") # instantiating person 2

print(person1.name)
print(person2.name)