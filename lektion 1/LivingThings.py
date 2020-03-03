class Person:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last
    
    def getName(self):
        return (self.firstName, self.lastName)

class Dog:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name