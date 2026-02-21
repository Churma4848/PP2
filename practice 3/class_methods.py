#methods are functions that belong to a classes

class Sultan:
    def __init__(self, age):
        self.age = age

    def holdru(self):
        print("I am " + self.age +"years old")

p = Sultan(27)
p.holdru()

#__str__() method

class Sultan:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"I am {self.age} years old"

p = Sultan(27)
p.holdru() 